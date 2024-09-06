#!/bin/bash
set -ex

if ! command -v gunicorn &> /dev/null
then
    echo "gunicorn 未安装，正在安装..."
    pip install gunicorn
fi
gunicorn -b '0.0.0.0:5000' -w 4 --threads 4  --reload  weibo:app
