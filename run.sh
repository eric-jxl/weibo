#!/bin/bash
set -e

if ! command -v gunicorn &> /dev/null
then
    echo "gunicorn 未安装"
	exit 1
fi
gunicorn -c config.py --access-logfile - --error-logfile - weibo:app
