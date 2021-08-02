from jupyter_rsession_proxy.handlers import setup_handlers

def _jupyter_server_extension_points():
    """
    Returns a list of dictionaries with metadata describing
    where to find the `_load_jupyter_server_extension` function.
    """
    return [{
        "module": "jupyter_rsession_proxy",
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "tree",
        "dest": "jupyter_rsession_proxy",
        "src": "static",
        "require": "jupyter_rsession_proxy/tree"
    }]

def _load_jupyter_server_extension(serverapp):
    setup_handlers(serverapp.web_app)

# Reference the old function name with the new function name.
load_jupyter_server_extension = _load_jupyter_server_extension
