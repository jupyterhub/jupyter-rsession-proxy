import getpass
import os
import pathlib
import shutil
import subprocess
import tempfile
import pwd
from textwrap import dedent
from urllib.parse import urlparse, urlunparse


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

def rewrite_auth(response, request):
    '''
       As of rstudio-server 1.4ish, it would send the client to /auth-sign-in
       rather than what the client sees as the full URL followed by
       /auth-sign-in. See rstudio/rstudio#8888. We rewrite the response by
       sending the client to the right place.
    '''
    for header, v in response.headers.get_all():
        if header == "Location" and v.startswith("/auth-sign-in"):
            # Visit the correct page
            u = urlparse(request.uri)
            response.headers[header] = urlunparse(u._replace(path=u.path+v))

def get_system_user():
    try:
        user = pwd.getpwuid(os.getuid())[0]
    except:
        user = os.environ.get('NB_USER', getpass.getuser())
    return(user)

def setup_rserver():
    def _get_env(port):
        return dict(USER=get_system_user())

    def db_config(db_dir):
        '''
        Create a temporary directory to hold rserver's database, and create
        the configuration file rserver uses to find the database.

        https://docs.rstudio.com/ide/server-pro/latest/database.html
        https://github.com/rstudio/rstudio/tree/v1.4.1103/src/cpp/server/db
        '''
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

    def _support_arg(arg):
        ret = subprocess.check_output([get_rstudio_executable('rserver'), '--help'])
        return ret.decode().find(arg) != -1

    def _get_cmd(port):
        ntf = tempfile.NamedTemporaryFile()

        # use mkdtemp() so the directory and its contents don't vanish when
        # we're out of scope
        server_data_dir = tempfile.mkdtemp()
        database_config_file = db_config(server_data_dir)

        cmd = [
            get_rstudio_executable('rserver'),
            '--auth-none=1',
            '--www-frame-origin=same',
            '--www-port=' + str(port),
            '--www-verify-user-agent=0',
            '--secure-cookie-key-file=' + ntf.name,
            '--server-user=' + get_system_user(),
        ]
        # Support at least v1.2.1335 and up

        if _support_arg('www-root-path'):
            cmd.append('--www-root-path={base_url}rstudio/')
        if _support_arg('server-data-dir'):
            cmd.append(f'--server-data-dir={server_data_dir}')
        if _support_arg('database-config-file'):
            cmd.append(f'--database-config-file={database_config_file}')

        return cmd

    def _get_timeout(default=15):
        return os.getenv('RSERVER_TIMEOUT', default)

    server_process = {
        'command': _get_cmd,
        'timeout': _get_timeout(),
        'environment': _get_env,
        'rewrite_response': rewrite_auth,
        'launcher_entry': {
            'title': 'RStudio',
            'icon_path': get_icon_path()
        }
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
            '--user-identity=' + get_system_user(),
            '--www-port=' + str(port)
        ]

    def _get_timeout(default=15):
        return os.getenv('RSESSION_TIMEOUT', default)

    return {
        'command': _get_cmd,
        'timeout': _get_timeout(),
        'environment': _get_env,
        'launcher_entry': {
            'title': 'RStudio',
            'icon_path': get_icon_path()
        }
    }
