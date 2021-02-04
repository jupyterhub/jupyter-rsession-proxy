import getpass
import os
import pathlib
import shutil
import subprocess
import tempfile
from textwrap import dedent

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
        '''Create a temporary directory to hold rserver's database.'''
        db_dir = tempfile.TemporaryDirectory()
        # create the rserver database config
        db_conf = dedent("""
            provider=sqlite
            directory={directory}
        """).format(directory=db_dir.name)
        f = tempfile.NamedTemporaryFile(mode='w', delete=False)
        db_config_name = f.name
        f.write(db_conf)
        f.close()
        return db_config_name

    def _get_cmd(port):
        cmd = [
            get_rstudio_executable('rserver'),
            '--auth-none=1',
            '--www-frame-origin=same',
            '--www-port=' + str(port),
            '--www-verify-user-agent=0'
        ]

        if os.environ.get('RSESSION_PROXY_DB_CONFIG', '0') != '0':
            cmd.append(f'--database-config-file={db_config()}')

        # Tell rserver what path it is being served from.
        # rserver's www-root-path option is present in RStudio >= 1.4. If this
        # environment variable is set to rserver's default, /, we don't set the
        # option. The value should be the name of our entry point which is
        # usually /rstudio/, however since people can add custom entry points,
        # we won't assume.
        www_root_path = os.environ.get('RSESSION_PROXY_WWW_ROOT_PATH', '/')
        if www_root_path != "/":
            hub_service_prefix = os.environ.get('JUPYTERHUB_SERVICE_PREFIX', '')
            root_path = pathlib.Path(hub_service_prefix + www_root_path)
            cmd.append(f'--www-root-path={root_path}/')

        return cmd

    return {
        'command': _get_cmd,
        'environment': _get_env,
        'launcher_entry': {
            'title': 'RStudio',
            'icon_path': get_icon_path()
        }
    }

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
