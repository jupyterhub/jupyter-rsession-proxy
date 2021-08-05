"""
jupyter-rsession-proxy setup
"""

import json
from pathlib import Path
import setuptools

from jupyter_packaging import (
    combine_commands,
    create_cmdclass,
    ensure_targets,
    install_npm,
    skip_if_exists,
)

HERE = Path(__file__).parent.resolve()

# The name of the project
name = "jupyter_rsession_proxy"

lab_path = HERE / name / "labextension"

# Representative files that should exist after a successful build
jstargets = [
    str(lab_path / "package.json"),
]

package_data_spec = {
    name: ["*"],
}

labext_name = "@jupyterlab/rsession-proxy"

data_files_spec = [
    ("share/jupyter/labextensions/%s" % labext_name, str(lab_path), "**"),
    ("share/jupyter/labextensions/%s" % labext_name, str(HERE), "install.json"),
    (
        "etc/jupyter/jupyter_server_config.d",
        "jupyter_rsession_proxy/etc",
        "jupyter-rsession-proxy-jupyterserverextension.json",
    ),
    (
        "etc/jupyter/jupyter_notebook_config.d",
        "jupyter_rsession_proxy/etc",
        "jupyter-rsession-proxy-notebookserverextension.json",
    ),
    (
        "etc/jupyter/nbconfig/tree.d",
        "jupyter_rsession_proxy/etc",
        "jupyter-rsession-proxy-nbextension.json",
    ),
]

cmdclass = create_cmdclass(
    "jsdeps", package_data_spec=package_data_spec, data_files_spec=data_files_spec
)

js_command = combine_commands(
    install_npm(HERE / "jupyterlab-rsession-proxy", build_cmd="build:prod", npm=["jlpm"]),
    ensure_targets(jstargets),
)

is_repo = (HERE / ".git").exists()
if is_repo:
    cmdclass["jsdeps"] = js_command
else:
    cmdclass["jsdeps"] = skip_if_exists(jstargets, js_command)

long_description = (HERE / "README.md").read_text()

# Get the package info from package.json
pkg_json = json.loads((HERE / "jupyterlab-rsession-proxy" / "package.json").read_bytes())

setup_args = dict(
    name=name.replace("_", "-"),
    version=pkg_json["version"],
    url=pkg_json["homepage"],
    author=pkg_json["author"]["name"],
    author_email=pkg_json["author"]["email"],
    description=pkg_json["description"],
    license=pkg_json["license"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    cmdclass=cmdclass,
    packages=setuptools.find_packages(),
    install_requires=[
        'jupyter-server-proxy>=3.1.0'
    ],
    include_package_data=True,
    keywords=["Jupyter", "JupyterLab", "JupyterLab3"],
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
    data_files=[
        (
            "share/jupyter/nbextensions/jupyter_rsession_proxy",
            ["jupyter_rsession_proxy/static/tree.js"],
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
    # Apparently it is sufficient for the icon to just be in MANIFEST.in, but
    # the docs say it should be in package_data. It is not sufficient to be in
    # package_data but not MANIFEST.in. ¯\_(ツ)_/¯
    package_data={
        'jupyter_rsession_proxy': ['icons/rstudio.svg', 'static/*'],
    },
)


if __name__ == "__main__":
    setuptools.setup(**setup_args)
