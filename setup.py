import setuptools

setuptools.setup(
    name="jupyter-rsession-proxy",
    version='2.0',
    url="https://github.com/jupyterhub/jupyter-rsession-proxy",
    author="Ryan Lovett & Yuvi Panda",
    description="Jupyter extension to proxy RStudio",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=3.1.0'
    ],
    package_data={
        'jupyter_rsession_proxy': ['icons/rstudio.svg'],
    },
)
