<div align="center">
    <img width="600" src="./logo.png" alt="ZmsAi" />
</div>

---

![Development Status](https://img.shields.io/badge/Under-Development-red) ![py3.8](https://camo.githubusercontent.com/f0cf3d008a2671b0a60a7bb65cbcd1adfdfc93f5e1d54032d3c64bad5a2f8a25/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e382d626c75652e737667) ![GPLv3](https://camo.githubusercontent.com/400c4e52df43f6a0ab8a89b74b1a78d1a64da56a7848b9110c9d2991bb7c3105/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d47504c76332d626c75652e737667)

[![Say Thanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/architdwivedi.off%40gmail.com) [![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A command line utility for topic discovery and doc-linking within the Zettelkasten using AI approaches.

## Test Run
Execute `run.sh` shell script to test run the project.
```bash
bash run.sh
```

## Manual
```shell
usage: zmsai [-h] [--path [PATH]] [--topics [TOPICS]] [--nwords [NWORDS]] [--distro [DISTRO]] [task]

positional arguments:
  task                  Provide task to perform [default : 'run'] [values : 'run', 'delete', 'display', 'man', 'test']

optional arguments:
  -h, --help            show this help message and exit
  --path [PATH], -p [PATH]
                        Provide directory of text files. [with : 'run'] [default : './custom']
  --topics [TOPICS], -t [TOPICS]
                        How many topics do you expect? [with : 'run'] [default : 'number of docs']
  --nwords [NWORDS], -w [NWORDS]
                        How many words per topic/doc do you want to display? [with : 'display'] [default : 5]
  --distro [DISTRO], -d [DISTRO]
                        What distributions do you want to display? [with : 'display'] [default : all] [values : 'dt', 'tw', 'dw', 'voc', 'all']
```

## Dependency Graph

```shell
attrs==20.2.0
  - pytest==6.1.1 [requires: attrs>=17.4.0]
iniconfig==1.1.1
  - pytest==6.1.1 [requires: iniconfig]
joblib==0.17.0
  - scikit-learn==0.23.2 [requires: joblib>=0.11]
    - sklearn==0.0 [requires: scikit-learn]
numpy==1.19.2
  - scikit-learn==0.23.2 [requires: numpy>=1.13.3]
    - sklearn==0.0 [requires: scikit-learn]
  - scipy==1.5.3 [requires: numpy>=1.14.5]
    - scikit-learn==0.23.2 [requires: scipy>=0.19.1]
      - sklearn==0.0 [requires: scikit-learn]
pip==20.1.1
pluggy==0.13.1
  - pytest==6.1.1 [requires: pluggy>=0.12,<1.0]
py==1.9.0
  - pytest==6.1.1 [requires: py>=1.8.2]
pyparsing==2.4.7
  - packaging==20.4 [requires: pyparsing>=2.0.2]
    - pytest==6.1.1 [requires: packaging]
setuptools==46.4.0
six==1.15.0
  - packaging==20.4 [requires: six]
    - pytest==6.1.1 [requires: packaging]
threadpoolctl==2.1.0
  - scikit-learn==0.23.2 [requires: threadpoolctl>=2.0.0]
    - sklearn==0.0 [requires: scikit-learn]
toml==0.10.1
  - pytest==6.1.1 [requires: toml]
wheel==0.34.2
```