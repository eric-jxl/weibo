#!/bin/bash
set -eux

gunicorn_path=$(which gunicorn)

$gunicorn_path -c config.py --access-logfile - --error-logfile - weibo:app
