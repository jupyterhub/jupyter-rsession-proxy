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

def rewrite_netloc(response, request):
    '''
       In some circumstances, rstudio-server appends a port to the URL while
       setting Location in the header. We rewrite the response to use the host
       in the request.
    '''
    for header, v in response.headers.get_all():
        if header == "Location":
            u = urlparse(v)
            if u.netloc != request.host:
                response.headers[header] = urlunparse(u._replace(netloc=request.host))

def get_system_user():
    try:
        user = pwd.getpwuid(os.getuid())[0]
    except:
        user = os.getenv('NB_USER', getpass.getuser())
    return(user)

def setup_rserver():
    def _get_env(port, unix_socket):
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

    def _support_args(args):
        ret = subprocess.check_output([get_rstudio_executable('rserver'), '--help'])
        help_output = ret.decode()
        return {arg: (help_output.find(f"--{arg}") != -1) for arg in args}

    def _get_www_frame_origin(default="same"):
        try:
            return os.getenv('JUPYTER_RSESSION_PROXY_WWW_FRAME_ORIGIN', default)
        except Exception:
            return default

    def _get_cmd(port, unix_socket):
        ntf = tempfile.NamedTemporaryFile()

        # use mkdtemp() so the directory and its contents don't vanish when
        # we're out of scope
        server_data_dir = tempfile.mkdtemp()
        database_config_file = db_config(server_data_dir)

        cmd = [
            get_rstudio_executable('rserver'),
            '--auth-none=1',
            '--www-frame-origin=' + _get_www_frame_origin(),
            '--www-verify-user-agent=0',
            '--secure-cookie-key-file=' + ntf.name,
            '--server-user=' + get_system_user(),
        ]
        # Support at least v1.2.1335 and up

        supported_args = _support_args([
            'www-root-path',
            'server-data-dir',
            'database-config-file',
            'www-thread-pool-size',
            'www-socket',
        ])
        if supported_args['www-root-path']:
            cmd.append('--www-root-path={base_url}rstudio/')
        if supported_args['server-data-dir']:
            cmd.append(f'--server-data-dir={server_data_dir}')
        if supported_args['database-config-file']:
            cmd.append(f'--database-config-file={database_config_file}')

        if supported_args['www-thread-pool-size']:
            thread_pool_size_env = os.getenv('JUPYTER_RSESSION_PROXY_THREAD_POOL_SIZE', None)
            try:
                if thread_pool_size_env is not None:
                    thread_pool_size = int(thread_pool_size_env)
                    if thread_pool_size > 0:
                        cmd.append('--www-thread-pool-size=' + str(thread_pool_size))
            except ValueError:
                print("Invalid value for JUPYTER_RSESSION_PROXY_THREAD_POOL_SIZE. Must be an integer.")
                pass

        if unix_socket != "":
            if supported_args['www-socket']:
                cmd.append('--www-socket={unix_socket}')
            else:
                raise NotImplementedError(f'rstudio-server does not support requested socket connection')
        else:
            cmd.append('--www-port={port}')

        return cmd

    def _get_timeout(default=15):
        try:
            return float(os.getenv('RSERVER_TIMEOUT', default))
        except Exception:
            return default

    server_process = {
        'command': _get_cmd,
        'timeout': _get_timeout(),
        'environment': _get_env,
        'rewrite_response': rewrite_netloc,
        'launcher_entry': {
            'title': 'RStudio',
            'icon_path': get_icon_path()
        }
    }

    use_socket = os.getenv('JUPYTER_RSESSION_PROXY_USE_SOCKET')
    if use_socket is not None:
        # If this env var is anything other than case insensitive 'no' or 'false',
        # use unix sockets instead of tcp sockets. This allows us to default to
        # using unix sockets by default in the future once this feature is better
        # tested, and allow people to turn it off if needed.
        if use_socket.casefold() not in ('no', 'false'):
            server_process['unix_socket'] = True

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
        try:
            return float(os.getenv('RSESSION_TIMEOUT', default))
        except Exception:
            return default

    return {
        'command': _get_cmd,
        'timeout': _get_timeout(),
        'environment': _get_env,
        'launcher_entry': {
            'title': 'RStudio',
            'icon_path': get_icon_path()
        }
    }
