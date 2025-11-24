# jupyter-rsession-proxy

[![TravisCI build status](https://img.shields.io/travis/com/jupyterhub/jupyter-rsession-proxy?logo=travis)](https://travis-ci.com/jupyterhub/jupyter-rsession-proxy)

**jupyter-rsession-proxy** provides Jupyter server and notebook extensions to proxy RStudio.

![Screenshot](screenshot.png)

If you have a JupyterHub deployment, jupyter-rsession-proxy can take advantage of JupyterHub's existing authenticator and spawner to launch RStudio in users' Jupyter environments. You can also run this from within Jupyter.
Note that [RStudio Server Pro](https://rstudio.com/products/rstudio-server-pro) has more featureful authentication and spawning than the standard version, in the event that you do not want to use Jupyter's.

This extension used to proxy Shiny server as well, however that functionality has been [separated](https://github.com/ryanlovett/jupyter-shiny-proxy).

## Installation

### Pre-reqs

#### Install rstudio
Use conda `conda install rstudio` or [download](https://www.rstudio.com/products/rstudio/download-server/) the corresponding package for your platform

Note that rstudio server is needed to work with this extension.

### Install jupyter-rsession-proxy

Install the library via `pip`:
```
pip install jupyter-rsession-proxy
```
Or via `conda`:
```
conda install -c conda-forge jupyter-rsession-proxy
```

### Traitlets configuration

You may also manually configure this extension inside a [traitlets](https://traitlets.readthedocs.io/en/stable/) configuration file for [jupyter-server-proxy](https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html#specifying-config-via-traitlets). This also allows you to configure multiple different RStudio applications, for instance using different versions of R:

```python
from jupyter_rsession_proxy import setup_rserver
# update the jupyter-server-proxy config by adding two RStudio servers
c.ServerProxy.servers.update({
  "rstudio1": setup_rserver(prefix="rstudio1", r_path="/usr/bin/R", launcher_title="RStudio (default R)"),
  "rstudio2": setup_rserver(prefix="rstudio2", r_path="/opt/miniconda3/bin/R", launcher_title="RStudio (other R)")
})
# note that the prefix and the dict key are the same for each server (both "rstudio1" and "rstudio2", respectively).
# this is necessary for everything to work correctly:
# if prefix and dict key differ, then the user would not be redirected to the right URL.
```

Note: in this scenario, `jupyter-rsession-proxy` must still first be installed (into the same environment as Jupyter) as described [above](#install-jupyter-rsession-proxy).


## Example

[rocker/binder](https://hub.docker.com/r/rocker/binder) contains an example installation which you can run on binder.

[![Launch binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rocker-org/binder/master?urlpath=rstudio)

### Multiuser Considerations

This extension launches an RStudio server process from the Jupyter notebook server. This is fine in JupyterHub deployments where user servers are containerized since other users cannot connect to the RStudio server port. In non-containerized JupyterHub deployments, for example on multiuser systems running LocalSpawner or BatchSpawner, this not secure. Any user may connect to Rstudio server and run arbitrary code.

## Configuration with Environment Variables
The following behavior can be configured with environment variables:

| Environment Variable                      | Effect                                                                | Default Value       | Notes                                                                     |
|-------------------------------------------|-----------------------------------------------------------------------|---------------------|---------------------------------------------------------------------------|
| `JUPYTER_RSESSION_PROXY_USE_SOCKET`       | Whether to use unix socket                                            | `true`                | By default a unix socket is used. If set to case-insensitive `no` or `false` it will switch to using a TCP socket |
| `JUPYTER_RSESSION_PROXY_WWW_FRAME_ORIGIN` | The value of the `www-frame-origin` flag to rserver                   | `same`              |                                                                           |
| `RSERVER_TIMEOUT`                         | Idle timeout flag to rserver in minutes                               | `15`                | Must be numeric and positive                                              |
| `RSESSION_TIMEOUT`                        | Idle timeout flag to rsession in minutes                              | `15`                | Must be numeric and positive                                              |
| `NB_USER`                                 | Fallback name of the Notebook user, if password database lookup fails | `getuser.getpass()` |                                                                           |
