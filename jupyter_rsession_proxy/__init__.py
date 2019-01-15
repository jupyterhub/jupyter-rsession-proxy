import os
import tempfile
import subprocess
import getpass
import shutil
from textwrap import dedent

def setup_shiny():
    '''Manage a Shiny instance.'''

    name = 'shiny'
    def _get_shiny_cmd(port):
        conf = dedent("""
            run_as {user};
            server {{
                listen {port};
                location / {{
                    site_dir {site_dir};
                    log_dir {site_dir}/logs;
                    directory_index on;
                }}
            }}
        """).format(
            user=getpass.getuser(),
            port=str(port),
            site_dir=os.getcwd()
        )

        f = tempfile.NamedTemporaryFile(mode='w', delete=False)
        f.write(conf)
        f.close()
        return ['shiny-server', f.name]

    return {
        'command': _get_shiny_cmd,
        'launcher_entry': {
            'title': 'Shiny',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'shiny.svg')
        }
    }

def setup_rstudio():
    def _get_rserver_cmd(port):
        # Other paths rsession maybe in
        other_paths = [
            # When rstudio-server deb is installed
            '/usr/lib/rstudio-server/bin/rserver',
            # When just rstudio deb is installed
            '/usr/lib/rstudio/bin/rserver',
        ]
        if shutil.which('rserver'):
            executable = 'rserver'
        else:
            for op in other_paths:
                if os.path.exists(op):
                    executable = op
                    break
            else:
                raise FileNotFoundError('Can not find rserver in PATH')

        return [
            executable,
            '--www-port=' + str(port)
        ]

    return {
        'command': _get_rserver_cmd,
        'environment': {
            'USER': getpass.getuser()
        },
        'launcher_entry': {
            'title': 'RStudio',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'rstudio.svg')
        }
    }