#!/bin/bash
set -e

if ! command -v gunicorn &> /dev/null
then
    echo "gunicorn 未安装，正在安装..."
    pip install gunicorn --user
fi
gunicorn -c config.py --access-logfile - --error-logfile - weibo:app
