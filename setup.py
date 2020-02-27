import setuptools

setuptools.setup(
    name="jupyter-rsession-proxy",
    version='1.0',
    url="https://github.com/jupyterhub/jupyter-rsession-proxy",
    author="Ryan Lovett & Yuvi Panda",
    description="Jupyter extension to proxy RStudio's rsession",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'rstudio = jupyter_rsession_proxy:setup_rstudio'
        ]
    },
    package_data={
        'jupyter_rsession_proxy': ['icons/rstudio.svg'],
    },
)
