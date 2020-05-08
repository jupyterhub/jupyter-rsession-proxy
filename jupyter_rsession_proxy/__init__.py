import os
import subprocess
import getpass
import shutil

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

    def _get_cmd(port):
        return [
            get_rstudio_executable('rserver'),
            '--www-port=' + str(port),
            '--www-frame-origin=same'
        ]

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
