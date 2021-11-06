import getpass
import os
import pathlib
import shutil
import subprocess
import tempfile
from textwrap import dedent

from tornado import httputil

def patch_redirect(request, host, port, path, response):
    '''Substitute a redirect to /auth-sign-in.'''
    headers = response.headers.get_all()
    newheaders = httputil.HTTPHeaders()
    for header, v in headers:
        if header == "Location" and v.startswith("/auth-sign-in"):
            # Visit the correct page
            newheaders.add(header, request.uri + v)
        else:
            newheaders.add(header, v)

    return dict(headers=newheaders)

def get_rstudio_executable(prog):
    # Find prog in known locations
    other_paths = [
        # When rstudio-server deb is installed
        os.path.join('/usr/lib/rstudio-server/bin', prog),
        # When just rstudio deb is installed
        os.path.join('/usr/lib/rstudio/bin', prog),
    ]
    if shutil.which(prog):
        return prog

    for op in other_paths:
        if os.path.exists(op):
            return op

    raise FileNotFoundError(f'Could not find {prog} in PATH')

def get_icon_path():
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icons', 'rstudio.svg'
    )

def setup_rserver():
    def _get_env(port):
        return dict(USER=getpass.getuser())

    def db_config():
        '''
        Create a temporary directory to hold rserver's database, and create
        the configuration file rserver uses to find the database.

        https://docs.rstudio.com/ide/server-pro/latest/database.html
        https://github.com/rstudio/rstudio/tree/v1.4.1103/src/cpp/server/db
        '''
        # use mkdtemp() so the directory and its contents don't vanish when
        # we're out of scope
        db_dir = tempfile.mkdtemp()
        # create the rserver database config
        db_conf = dedent("""
            provider=sqlite
            directory={directory}
        """).format(directory=db_dir)
        f = tempfile.NamedTemporaryFile(mode='w', delete=False, dir=db_dir)
        db_config_name = f.name
        f.write(db_conf)
        f.close()
        return db_config_name

    def _get_cmd(port):
        cmd = [
            get_rstudio_executable('rserver'),
            '--auth-none=1',
            f'--server-user={getpass.getuser()}',
            '--www-frame-origin=same',
            '--www-port=' + str(port),
            '--www-verify-user-agent=0',
            '--www-root-path={base_url}rstudio/',
            f'--database-config-file={db_config()}'
        ]

        return cmd

    server_process = {
        'command': _get_cmd,
        'environment': _get_env,
        'launcher_entry': {
            'title': 'RStudio',
            'icon_path': get_icon_path()
        },
        'rewrite_response': patch_redirect,
    }

    return server_process

def setup_rsession():
    def _get_env(port):
        # Detect various environment variables rsession requires to run
        # Via rstudio's src/cpp/core/r_util/REnvironmentPosix.cpp
        cmd = ['R', '--slave', '--vanilla', '-e',
                'cat(paste(R.home("home"),R.home("share"),R.home("include"),R.home("doc"),getRversion(),sep=":"))']

        r_output = subprocess.check_output(cmd)
        R_HOME, R_SHARE_DIR, R_INCLUDE_DIR, R_DOC_DIR, version = \
            r_output.decode().split(':')

        return {
            'R_DOC_DIR': R_DOC_DIR,
            'R_HOME': R_HOME,
            'R_INCLUDE_DIR': R_INCLUDE_DIR,
            'R_SHARE_DIR': R_SHARE_DIR,
            'RSTUDIO_DEFAULT_R_VERSION_HOME': R_HOME,
            'RSTUDIO_DEFAULT_R_VERSION': version,
        }

    def _get_cmd(port):
        return [
            get_rstudio_executable('rsession'),
            '--standalone=1',
            '--program-mode=server',
            '--log-stderr=1',
            '--session-timeout-minutes=0',
            '--user-identity=' + getpass.getuser(),
            '--www-port=' + str(port)
        ]

    return {
        'command': _get_cmd,
        'environment': _get_env,
        'launcher_entry': {
            'title': 'RStudio',
            'icon_path': get_icon_path()
        }
    }
