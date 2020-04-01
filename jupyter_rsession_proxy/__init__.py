"""
This file contains logic that is required for "jupyter-server-proxy" to register additional launchers in Jupyter Notebook.
Docs: https://github.com/jupyterhub/jupyter-server-proxy/blob/master/docs/server-process.rst
"""
import getpass
import os
import shlex
import shutil
import subprocess


# RSTUDIO_RSERVER_BIN - Prioritized location for searching binary file "rserver". 
# Should be an absolute path to rserver or not set.
RSTUDIO_RSERVER_BIN = os.getenv('RSTUDIO_RSERVER_BIN')

# RSTUDIO_RSERVER_ARGS - Overrides all arguments (except --www-port) for "rserver" binary.
# Should be an absolute path to rserver or not set.
RSTUDIO_RSERVER_ARGS = os.getenv('RSTUDIO_RSERVER_ARGS', '')

# RSTUDIO_RSESSION_BIN - Prioritized location for searching binary file "rsession". 
RSTUDIO_RSESSION_BIN = os.getenv('RSTUDIO_RSESSION_BIN')

# RSTUDIO_RSESSION_ARGS - Overrides all arguments (except --www-port and --user-identity) for "rsession" binary.
RSTUDIO_RSESSION_ARGS = os.getenv(
    'RSTUDIO_RSESSION_ARGS', 
    '--standalone=1 --program-mode=server --log-stderr=1 --session-timeout-minutes=0'
)

# RSTUDIO_FOLDER - Prioritized folder for searching all RStudio related binary files.
# Should be an absolute path to folder or not set.
RSTUDIO_FOLDER = os.getenv('RSTUDIO_FOLDER')


def get_rstudio_executable(prog):
    """Find location (absolute path) of RStudio program"""
    # Try env. variable RSTUDIO_FOLDER to search prog in
    if RSTUDIO_FOLDER:
        bin_location = os.path.join(RSTUDIO_FOLDER, prog)
        if os.path.exists(bin_location):
            return bin_location

    # Find prog in known locations
    other_paths = [
        # When rstudio-server deb is installed
        os.path.join('/usr/lib/rstudio-server/bin', prog),
        # When just rstudio deb is installed
        os.path.join('/usr/lib/rstudio/bin', prog),
    ]
    
    # Try to find prog in PATH
    if shutil.which(prog):
        return prog

    for op in other_paths:
        if os.path.exists(op):
            return op

    raise FileNotFoundError(f'Could not find {prog} in PATH or well known locations')

def get_icon_path():
    """Get path to icon for Jupyter web interface"""
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icons', 'rstudio.svg'
    )

def setup_rserver():
    """Get entry for RServer"""
    def _get_env(port):
        return dict(USER=getpass.getuser())

    def _get_cmd(port):
        bin_file = RSTUDIO_RSERVER_BIN if RSTUDIO_RSERVER_BIN else get_rstudio_executable('rserver')
        cmd = [
            bin_file,
            '--www-port=' + str(port)
        ]
        if RSTUDIO_RSERVER_ARGS:
            cmd.extend(shlex.split(RSTUDIO_RSERVER_ARGS))
        return cmd

    return {
        'command': _get_cmd,
        'environment': _get_env,
        'launcher_entry': {
            'title': 'RStudio Server',
            'icon_path': get_icon_path()
        }
    }

def setup_rsession():
    """Get entry for RSession"""
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
        bin_file = RSTUDIO_RSESSION_BIN if RSTUDIO_RSESSION_BIN else get_rstudio_executable('rsession')
        cmd = [
            bin_file,
            '--user-identity=' + getpass.getuser(),
            '--www-port=' + str(port)
        ]
        if RSTUDIO_RSESSION_ARGS:
            cmd.extend(shlex.split(RSTUDIO_RSESSION_ARGS))
        return cmd

    return {
        'command': _get_cmd,
        'environment': _get_env,
        'launcher_entry': {
            'title': 'RStudio Session',
            'icon_path': get_icon_path()
        }
    }
