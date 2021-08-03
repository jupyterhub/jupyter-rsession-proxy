import setuptools

# The name of the project
name = "jupyter_rsession_proxy"

setup_args = dict(
    name=name.replace("_", "-"),
    version='2.0',
    url="https://github.com/jupyterhub/jupyter-rsession-proxy",
    author="Ryan Lovett & Yuvi Panda",
    description="Jupyter extension to proxy RStudio",
    packages=setuptools.find_packages(),
    keywords=["Jupyter"],
    classifiers=[
        "Framework :: Jupyter",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        'jupyter-server-proxy>=3.1.0'
    ],
    include_package_data=True,
    data_files=[
        (
            "share/jupyter/nbextensions/jupyter_rsession_proxy",
            ["jupyter_rsession_proxy/static/tree.js"]
        ),
        (
            "etc/jupyter/jupyter_notebook_config.d",
            ["jupyter_rsession_proxy/etc/jupyter-rsession-proxy-notebookserverextension.json"],
        ),
        (
            "etc/jupyter/jupyter_server_config.d",
            ["jupyter_rsession_proxy/etc/jupyter-rsession-proxy-jupyterserverextension.json"],
        ),
        (
            "etc/jupyter/nbconfig/tree.d",
            ["jupyter_rsession_proxy/etc/jupyter-rsession-proxy-nbextension.json"],
        ),
    ],
    package_data={
        'jupyter_rsession_proxy': ['icons/rstudio.svg', 'static/*'],
    },
)


if __name__ == "__main__":
    setuptools.setup(**setup_args)
