#!/usr/bin/env bash

function start () {
  ENV_PATH=$(pipenv --venv)
#  echo "$ENV_PATH"
  if [[ -z "$ENV_PATH" ]]; then
      echo "Install new environment (./install.sh) before run this project "
  else
      source "$ENV_PATH/bin/activate"
      gunicorn -b 127.0.0.1:5000 --reload customer.app:app --log-level DEBUG
  fi
}

function stop () {
    ps -ef | grep gunicorn | awk '{print $2}' | xargs kill -9
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    *)
    echo "Usage: run.sh {start|stop}"
    exit 1
esac