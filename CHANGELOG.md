# Changelog

## 2.5

### v2.5.1 - 2026-05-11

([full changelog](https://github.com/jupyterhub/jupyter-rsession-proxy/compare/v2.5.0...5754f90cf53db72c0b4dd2e032152cd0265edede))

#### Bugs fixed

- Fix root path regression [#179](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/179) ([@jrdnbradford](https://github.com/jrdnbradford), [@ryanlovett](https://github.com/ryanlovett))

#### Contributors to this release

The following people contributed discussions, new ideas, code and documentation contributions, and review.
See [our definition of contributors](https://github-activity.readthedocs.io/en/latest/use/#how-does-this-tool-define-contributions-in-the-reports).

([GitHub contributors page for this release](https://github.com/jupyterhub/jupyter-rsession-proxy/graphs/contributors?from=2026-04-28&to=2026-05-11&type=c))

@jrdnbradford ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Ajrdnbradford+updated%3A2026-04-28..2026-05-11&type=Issues)) | @ryanlovett ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aryanlovett+updated%3A2026-04-28..2026-05-11&type=Issues))

### v2.5.0 - 2026-04-28

([full changelog](https://github.com/jupyterhub/jupyter-rsession-proxy/compare/ff8e103044c7bedf304243846f43f5d1b0e7179f...341bfa93f8f572c64ef89b998b9bd3db0e700d8e))

#### Maintenance and upkeep improvements

- Secure server_data_dir creation with nested temp dir [#173](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/173) ([@dometto](https://github.com/dometto), [@minrk](https://github.com/minrk))

#### Documentation improvements

- Update security note for RStudio server deployment [#171](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/171) ([@dometto](https://github.com/dometto), [@consideRatio](https://github.com/consideRatio), [@minrk](https://github.com/minrk))

#### Continuous integration improvements

- Bump actions/checkout from 5 to 6 [#174](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/174) ([@consideRatio](https://github.com/consideRatio))

#### Other merged PRs

- Allow specifying server prefix and R path [#170](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/170) ([@dometto](https://github.com/dometto), [@ryanlovett](https://github.com/ryanlovett))

#### Contributors to this release

The following people contributed discussions, new ideas, code and documentation contributions, and review.
See [our definition of contributors](https://github-activity.readthedocs.io/en/latest/use/#how-does-this-tool-define-contributions-in-the-reports).

([GitHub contributors page for this release](https://github.com/jupyterhub/jupyter-rsession-proxy/graphs/contributors?from=2025-11-19&to=2026-04-17&type=c))

@consideRatio ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3AconsideRatio+updated%3A2025-11-19..2026-04-17&type=Issues)) | @dometto ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Adometto+updated%3A2025-11-19..2026-04-17&type=Issues)) | @minrk ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aminrk+updated%3A2025-11-19..2026-04-17&type=Issues)) | @ryanlovett ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aryanlovett+updated%3A2025-11-19..2026-04-17&type=Issues))

## 2.4

### v2.4.0 - 2025-11-18

([full changelog](https://github.com/jupyterhub/jupyter-rsession-proxy/compare/v2.3.0...v2.4.0))

#### Enhancements made

- Make unix socket default [#166](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/166) ([@jrdnbradford](https://github.com/jrdnbradford), [@yuvipanda](https://github.com/yuvipanda))

#### Bugs fixed

- Add handling for relative paths in Location headers [#157](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/157) ([@paulkm](https://github.com/paulkm), [@ryanlovett](https://github.com/ryanlovett))

#### Documentation improvements

- Add `JUPYTER_RSESSION_PROXY_USE_SOCKET` docs [#165](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/165) ([@jrdnbradford](https://github.com/jrdnbradford), [@consideRatio](https://github.com/consideRatio))
- fix: correct broken link in contributing [#163](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/163) ([@agoose77](https://github.com/agoose77), [@sgibson91](https://github.com/sgibson91))

#### Continuous integration improvements

- Bump actions/checkout from 4 to 5 [#168](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/168) ([@consideRatio](https://github.com/consideRatio))
- Bump actions/setup-python from 5 to 6 [#167](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/167) ([@consideRatio](https://github.com/consideRatio))

#### Contributors to this release

The following people contributed discussions, new ideas, code and documentation contributions, and review.
See [our definition of contributors](https://github-activity.readthedocs.io/en/latest/#how-does-this-tool-define-contributions-in-the-reports).

([GitHub contributors page for this release](https://github.com/jupyterhub/jupyter-rsession-proxy/graphs/contributors?from=2025-01-14&to=2025-11-18&type=c))

@agoose77 ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aagoose77+updated%3A2025-01-14..2025-11-18&type=Issues)) | @consideRatio ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3AconsideRatio+updated%3A2025-01-14..2025-11-18&type=Issues)) | @jrdnbradford ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Ajrdnbradford+updated%3A2025-01-14..2025-11-18&type=Issues)) | @paulkm ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Apaulkm+updated%3A2025-01-14..2025-11-18&type=Issues)) | @ryanlovett ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aryanlovett+updated%3A2025-01-14..2025-11-18&type=Issues)) | @sgibson91 ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Asgibson91+updated%3A2025-01-14..2025-11-18&type=Issues)) | @yuvipanda ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Ayuvipanda+updated%3A2025-01-14..2025-11-18&type=Issues))

## 2.3

### v2.3.0 - 2025-01-14

([full changelog](https://github.com/jupyterhub/jupyter-rsession-proxy/compare/v2.2.1...v2.3.0))

#### Enhancements made

- Support communicating with rstudio via unix socket instead of tcp socket [#159](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/159) ([@jhgoebbert](https://github.com/jhgoebbert))
- Made the www-frame-origin for rserver environment-configurable [#148](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/148) ([@rickmcgeer](https://github.com/rickmcgeer))

#### Maintenance and upkeep improvements

- update install requirement (jupyter-server-proxy) for unix-socket-support [#162](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/162) ([@jhgoebbert](https://github.com/jhgoebbert))
- minimize overhead when checking the supported args by RStudio [#160](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/160) ([@jhgoebbert](https://github.com/jhgoebbert))
- Add and document release automation via github actions [#155](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/155) ([@consideRatio](https://github.com/consideRatio))
- Update requirements for jupyter-server-proxy [#146](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/146) ([@consideRatio](https://github.com/consideRatio))

#### Documentation improvements

- Retroactively add v2.2.1 to changelog and fix heading levels etc [#154](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/154) ([@consideRatio](https://github.com/consideRatio))

#### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterhub/jupyter-rsession-proxy/graphs/contributors?from=2024-03-13&to=2025-01-14&type=c))

[@benz0li](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Abenz0li+updated%3A2024-03-13..2025-01-14&type=Issues) | [@consideRatio](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3AconsideRatio+updated%3A2024-03-13..2025-01-14&type=Issues) | [@jhgoebbert](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Ajhgoebbert+updated%3A2024-03-13..2025-01-14&type=Issues) | [@rickmcgeer](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Arickmcgeer+updated%3A2024-03-13..2025-01-14&type=Issues) | [@ryanlovett](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aryanlovett+updated%3A2024-03-13..2025-01-14&type=Issues) | [@welcome](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Awelcome+updated%3A2024-03-13..2025-01-14&type=Issues) | [@yuvipanda](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Ayuvipanda+updated%3A2024-03-13..2025-01-14&type=Issues)

## 2.2

### 2.2.1 - 2024-03-13

([full changelog](https://github.com/jupyterhub/jupyter-rsession-proxy/compare/v2.2.0...v2.2.1))

#### Merged PRs

- Update requirements for jupyter-server-proxy [#146](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/146) ([@consideRatio](https://github.com/consideRatio), [@ryanlovett](https://github.com/ryanlovett))
- Add new RStudio icon [#125](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/125) ([@danilopeixoto](https://github.com/danilopeixoto), [@yuvipanda](https://github.com/yuvipanda))

#### Contributors to this release

The following people contributed discussions, new ideas, code and documentation contributions, and review.
See [our definition of contributors](https://github-activity.readthedocs.io/en/latest/#how-does-this-tool-define-contributions-in-the-reports).

([GitHub contributors page for this release](https://github.com/jupyterhub/jupyter-rsession-proxy/graphs/contributors?from=2023-06-23&to=2024-03-13&type=c))

@benz0li ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Abenz0li+updated%3A2023-06-23..2024-03-13&type=Issues)) | @danilopeixoto ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Adanilopeixoto+updated%3A2023-06-23..2024-03-13&type=Issues)) | @eeholmes ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aeeholmes+updated%3A2023-06-23..2024-03-13&type=Issues)) | @ryanlovett ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aryanlovett+updated%3A2023-06-23..2024-03-13&type=Issues)) | @yuvipanda ([activity](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Ayuvipanda+updated%3A2023-06-23..2024-03-13&type=Issues))

### 2.2.0 - 2023-06-12

([full changelog](https://github.com/jupyterhub/jupyter-rsession-proxy/compare/v2.1.0...8a87f3fbb21015927cfb30aec63af791fb0a19bc))

#### Merged PRs

- Prepare 2.2.0 release. [#141](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/141) ([@ryanlovett](https://github.com/ryanlovett))
- add float conversion for timeout [#137](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/137) ([@matuskosut](https://github.com/matuskosut))
- Fix netloc when rstudio-server inserts port. [#134](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/134) ([@ryanlovett](https://github.com/ryanlovett))

#### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterhub/jupyter-rsession-proxy/graphs/contributors?from=2022-09-07&to=2023-06-12&type=c))

[@matuskosut](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Amatuskosut+updated%3A2022-09-07..2023-06-12&type=Issues) | [@ryanlovett](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aryanlovett+updated%3A2022-09-07..2023-06-12&type=Issues) | [@welcome](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Awelcome+updated%3A2022-09-07..2023-06-12&type=Issues)

## 2.1

### 2.1.0 - 2022-09-07

([full changelog](https://github.com/jupyterhub/jupyter-rsession-proxy/compare/v2.0...v2.1.0))

#### Merged PRs

- use NB_USER rather than getpass.getuser() [#132](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/132) ([@vivian-rook](https://github.com/vivian-rook))
- add 10s default timeout and environment varariable [#128](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/128) ([@matuskosut](https://github.com/matuskosut))
- Fix server data dir (/var/run/rstudio) not writable. Support multiple rstudio-server versions [#119](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/119) ([@ccoulombe](https://github.com/ccoulombe))
- Bump to 2.0.1. [#117](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/117) ([@ryanlovett](https://github.com/ryanlovett))
- Do not append the Location path to the whole uri. [#116](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/116) ([@ryanlovett](https://github.com/ryanlovett))
- Add CHANGELOG.md. [#112](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/112) ([@ryanlovett](https://github.com/ryanlovett))
- Add conda install instructions [#68](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/68) ([@xhochy](https://github.com/xhochy))

#### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterhub/jupyter-rsession-proxy/graphs/contributors?from=2021-12-01&to=2022-09-07&type=c))

[@ccoulombe](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Accoulombe+updated%3A2021-12-01..2022-09-07&type=Issues) | [@guimou](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aguimou+updated%3A2021-12-01..2022-09-07&type=Issues) | [@lucianolacurcia](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Alucianolacurcia+updated%3A2021-12-01..2022-09-07&type=Issues) | [@mathematicalmichael](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Amathematicalmichael+updated%3A2021-12-01..2022-09-07&type=Issues) | [@matuskosut](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Amatuskosut+updated%3A2021-12-01..2022-09-07&type=Issues) | [@moschlar](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Amoschlar+updated%3A2021-12-01..2022-09-07&type=Issues) | [@riazarbi](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Ariazarbi+updated%3A2021-12-01..2022-09-07&type=Issues) | [@ryanlovett](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aryanlovett+updated%3A2021-12-01..2022-09-07&type=Issues) | [@vivian-rook](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Avivian-rook+updated%3A2021-12-01..2022-09-07&type=Issues) | [@welcome](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Awelcome+updated%3A2021-12-01..2022-09-07&type=Issues) | [@xhochy](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Axhochy+updated%3A2021-12-01..2022-09-07&type=Issues) | [@yuvipanda](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Ayuvipanda+updated%3A2021-12-01..2022-09-07&type=Issues)

## 2.0

### 2.0 - 2021-12-01

#### BREAKING CHANGES

* Install a newer version of rstudio-server -- either a later 1.4 or a newer date-based release. If you are using an older versions of rstudio-server, please install jupyter-rsession-proxy <= 1.4. It is no longer necessary to set the RSESSION_PROXY_RSTUDIO_1_4 environment variable for this version.

#### Enhancements made

* Support recent rstudio-server releases.

#### Dependency updates

* Bump jupyter-server-proxy from 3.1.0 to 3.2.0.

#### Merged PRs

* Rewrite /auth-sign-in redirect. [#110](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/110) ([@ryanlovett](https://github.com/ryanlovett))
* Bump to v1.4. [#105](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/105) ([@ryanlovett](https://github.com/ryanlovett))
* Use tmp file for secure cookie [#98](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/98) ([@danielfrg](https://github.com/danielfrg))

#### Contributors to this release

([GitHub contributors page for this release](https://github.com/jupyterhub/jupyter-rsession-proxy/graphs/contributors?from=2021-07-03&to=2021-11-30&type=c))

[@danielfrg](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Adanielfrg+updated%3A2021-07-03..2021-11-30&type=Issues) | [@dhirschfeld](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Adhirschfeld+updated%3A2021-07-03..2021-11-30&type=Issues) | [@garyburgmann](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Agaryburgmann+updated%3A2021-07-03..2021-11-30&type=Issues) | [@JamesSample](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3AJamesSample+updated%3A2021-07-03..2021-11-30&type=Issues) | [@meeseeksmachine](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Ameeseeksmachine+updated%3A2021-07-03..2021-11-30&type=Issues) | [@orboan](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aorboan+updated%3A2021-07-03..2021-11-30&type=Issues) | [@riazarbi](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Ariazarbi+updated%3A2021-07-03..2021-11-30&type=Issues) | [@ryanlovett](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Aryanlovett+updated%3A2021-07-03..2021-11-30&type=Issues) | [@vnijs](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Avnijs+updated%3A2021-07-03..2021-11-30&type=Issues) | [@welcome](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Awelcome+updated%3A2021-07-03..2021-11-30&type=Issues) | [@yuvipanda](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Ayuvipanda+updated%3A2021-07-03..2021-11-30&type=Issues) | [@zeehio](https://github.com/search?q=repo%3Ajupyterhub%2Fjupyter-rsession-proxy+involves%3Azeehio+updated%3A2021-07-03..2021-11-30&type=Issues)

([full changelog](https://github.com/jupyterhub/jupyter-rsession-proxy/compare/3c6e224...526eeab29e9f8d88fa61a8d60d41e3812b47bd43))

This document was partially generated by [github-activity](https://github.com/executablebooks/github-activity).
