from jupyter_server_proxy.handlers import setup_handlers

# Jupyter Extension points
def _jupyter_server_extension_points():
    return [{
        'module': 'jupyter_rsession_proxy',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "tree",
        "dest": "jupyter_rsession_proxy",
        "src": "static",
        "require": "jupyter_rsession_proxy/tree"
    }]

def _load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.webapp)

# For backward compatibility
load_jupyter_server_extension = _load_jupyter_server_extension
