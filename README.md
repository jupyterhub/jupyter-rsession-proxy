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

## Example

[rocker/binder](https://hub.docker.com/r/rocker/binder) contains an example installation which you can run on binder.

[![Launch binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rocker-org/binder/master?urlpath=rstudio)

### Multiuser Considerations

This extension launches an rstudio server process from the jupyter notebook server. This is fine in JupyterHub deployments where user servers are containerized since other users cannot connect to the rstudio server port. In non-containerized JupyterHub deployments, for example on multiuser systems running LocalSpawner or BatchSpawner, this not secure. Any user may connect to rstudio server and run arbitrary code.

## Configuration with Environment Variables
The following behavior can be configured with environment variables

| Environment Variable | Effect | Default Value | Notes
| JUPYTER_RSESSION_PROXY_WWW_FRAME_ORIGIN | The value of the `www-frame-origin` flag to rserver | `same` | |
| RSERVER_TIMEOUT | Idle timeout flag to rserver in minutes | 15 | must be numeric and positive |
| RSESSION_TIMEOUT | Idle timeout flag to rsession in minutes | 15 | must be numeric and positive |
| NB_USER | Fallback name of the Notebook user, if password database lookup fails | `getuser.getpass()` ||
