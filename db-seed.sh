#!/bin/bash

ENV_PATH=$(pipenv --venv)
#echo "$ENV_PATH"
if [[ -z "$ENV_PATH" ]]; then
    echo "Install new environment (./install.sh) before run db-seed.sh"
else
    source "$ENV_PATH/bin/activate"
    python customer/fake_data.py
fi