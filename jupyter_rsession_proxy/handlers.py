# vim: set et sw=4 ts=4:
import getpass
import os
import shutil
import subprocess
import tempfile
from textwrap import dedent

from jupyter_server.utils import url_path_join as ujoin
from jupyter_server_proxy.handlers import SuperviseAndProxyHandler, AddSlashHandler
from jupyter_server_proxy.api import IconHandler

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

    raise FileNotFoundError(f'Could not find {prog} in $PATH or other common rstudio locations')

def get_icon_path():
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icons', 'rstudio.svg'
    )

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
    db_conf = dedent(f"""
        provider=sqlite
        directory={db_dir}
    """)
    db_config_name = os.path.join(db_dir, "database.conf")
    f = open(db_config_name, 'w')
    f.write(db_conf)
    f.close()
    return db_config_name

def detect_version():
    '''
    Detect version of rserver by running rsession. rserver does not have a
    version flag. They are typically (always?) installed from the same
    package.
    '''
    cmd = [get_rstudio_executable('rsession'), '--version']
    output = subprocess.check_output(cmd)
    version, rest = output.decode().split(',', 1)
    return version

class RSessionProxyHandler(SuperviseAndProxyHandler):
    '''Manage an RStudio rsession instance.'''

    name = 'RSession'

    def get_env(self):
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

    def get_cmd(self):
        return [
            get_rstudio_executable('rsession'),
            '--standalone=1',
            '--program-mode=server',
            '--log-stderr=1',
            '--session-timeout-minutes=0',
            '--user-identity=' + getpass.getuser(),
            '--www-port=' + str(self.port)
        ]

class RServerProxyHandler(SuperviseAndProxyHandler):
    '''Manage an RStudio rserver instance.'''

    name = 'RStudio'

    def initialize(self, state, version_ge_1_4):
        self.version_ge_1_4 = version_ge_1_4
        super().initialize(state)

    def get_env(self):
        return dict(USER=getpass.getuser())

    def get_cmd(self):
        cmd = [
            get_rstudio_executable('rserver'),
            '--auth-none=1',
            '--www-frame-origin=same',
            '--www-port=' + str(self.port),
            '--www-verify-user-agent=0'
        ]

        # Add additional options for RStudio >= 1.4.x.
        if self.version_ge_1_4:
            # base_url has a trailing slash
            cmd.append(f'--www-root-path={self.base_url}rstudio/')
            cmd.append(f'--database-config-file={db_config()}')

        return cmd

    async def http_get(self, path):
        if not self.version_ge_1_4 or "auth-sign-in" in path:
            return await super().http_get(path)

        cookie = self.request.headers.get('Cookie')
        if cookie and 'user-id' in cookie:
            return await super().http_get(path)
        else:
            auth_sign_in_url = f"{self.base_url}rstudio/auth-sign-in"
            self.log.info(f"No user-id in cookie. redirect to {auth_sign_in_url}")
            self.redirect(auth_sign_in_url)

def setup_handlers(web_app):
    base_url = web_app.settings['base_url']

    # rstudio-server ~ 1.4 introduced the auth-sign-in and root-path issues.
    # We try to detect the version, however the rsession version flag is
    # only in rstudio server 1.4.1717 and later. We still let the admin
    # inform us with an environment variable.'''
    version_ge_1_4 = os.environ.get('RSESSION_PROXY_RSTUDIO_1_4', False)
    try:
        detect_version()
    except:
        pass
    finally:
        version_ge_1_4 = True

    handlers = [
        (ujoin(base_url, 'rstudio', r'(.*)'), RServerProxyHandler, dict(state={}, version_ge_1_4=version_ge_1_4)),
        (ujoin(base_url, 'rstudio'), AddSlashHandler),
        (ujoin(base_url, 'rsession-proxy/icon/(.*)'), IconHandler, dict(icons={'rstudio':get_icon_path()}))
    ]

    web_app.add_handlers('.*', handlers)
