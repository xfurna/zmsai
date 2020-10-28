#!/bin/bash
pip3 install pipenv
pipenv install --dev
pipenv run python3 zmsai run -t 5
pipenv run python3 zmsai display --distro all
