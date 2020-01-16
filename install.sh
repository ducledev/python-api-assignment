#!/bin/bash

export PIPENV_VENV_IN_PROJECT=1
pipenv install
ENV_PATH=$(pipenv --venv)
#echo "$ENV_PATH"
source "$ENV_PATH/bin/activate"
