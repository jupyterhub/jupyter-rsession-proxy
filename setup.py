import setuptools

setuptools.setup(
    name='jupyter-rsession-proxy',
    version='1.2',
    url='https://github.com/jupyterhub/jupyter-rsession-proxy',
    author='Ryan Lovett & Yuvi Panda & Kirill Makhonin',
    description='Jupyter extension to proxy RStudio',
    packages=setuptools.find_packages(),
    keywords=['Jupyter'],
    classifiers=[
        'Framework :: Jupyter',
        'Programming Language :: Python :: 3'
    ],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'rstudio = jupyter_rsession_proxy:setup_rserver',
            'rsession = jupyter_rsession_proxy:setup_rsession'
        ]
    },
    package_data={
        'jupyter_rsession_proxy': ['icons/rstudio.svg'],
    },
)
