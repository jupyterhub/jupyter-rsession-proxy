# jupyter-rsession-proxy

[![PyPI](https://img.shields.io/pypi/v/jupyter-rsession-proxy?label=PyPI%20Version)](https://pypi.org/project/jupyter-rsession-proxy/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/jupyter-rsession-proxy)](https://pypi.org/project/jupyter-rsession-proxy/)

**jupyter-rsession-proxy** provides Jupyter server and notebook extensions to proxy RStudio Server (multi-user env.) or RStudio Session (single-user env.).

![Screenshot](screenshot.png)

If you have a JupyterHub deployment, jupyter-rsession-proxy can take advantage of JupyterHub's existing authenticator and spawner to launch RStudio in users' Jupyter environments. You can also run this from within Jupyter.
Note that [RStudio Server Pro](https://www.rstudio.com/products/rstudio-server-pro/architecture) has more featureful authentication and spawning than the standard version, in the event that you do not want to use Jupyter's.

This extension used to proxy Shiny server as well, however that functionality has been [separated](https://github.com/ryanlovett/jupyter-shiny-proxy).

## Installation

### Pre-reqs

#### Install rstudio
Use conda `conda install rstudio` or [download](https://www.rstudio.com/products/rstudio/download-server/) the corresponding package for your platform 

Note that rstudio server is needed to work with this extension.

### Install jupyter-rsession-proxy

Install the library:
```
pip install jupyter-rsession-proxy
```

## Configuring using environment variables

This extension can be configured using environment variables. 
Below is a list with all supported environment variables.

| Environment variable  | Description |
| --------------------- |-------------| 
| RSTUDIO_RSERVER_BIN   | Prioritized location for searching binary file "rserver". Should be an absolute path to rserver or not set. | 
| RSTUDIO_RSERVER_ARGS  | Overrides all arguments (except --www-port) for "rserver" binary. | 
| RSTUDIO_RSESSION_BIN  | Prioritized location for searching binary file "rsession". Should be an absolute path to rserver or not set. |
| RSTUDIO_RSESSION_ARGS | Overrides all arguments (except --www-port and --user-identity) for "rsession" binary. |
| RSTUDIO_FOLDER        | Prioritized folder for searching all RStudio related binary files. Should be an absolute path to folder or not set. |


## Example

[rocker/binder](https://hub.docker.com/r/rocker/binder) contains an example installation which you can run on binder.

[![Launch binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rocker-org/binder/master?urlpath=rstudio)

### Multiuser Considerations

This extension launches an rstudio server process from the jupyter notebook server. This is fine in JupyterHub deployments where user servers are containerized since other users cannot connect to the rstudio server port. In non-containerized JupyterHub deployments, for example on multiuser systems running LocalSpawner or BatchSpawner, this not secure. Any user may connect to rstudio server and run arbitrary code.
