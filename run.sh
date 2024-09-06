#!/bin/bash
set -x

gunicorn -c config.py --access-logfile - --error-logfile - weibo:app
