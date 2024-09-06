#!/usr/bin/env python3

import multiprocessing
import os
import gevent.monkey
gevent.monkey.patch_all()


# debug = True
bind = "0.0.0.0:5000"
pidfile = "log/gunicorn.pid"
timeout = 30

loglevel = 'info'
accesslog = "log/access.log"
errorlog = "log/debug.log"
daemon = False
preload_app = True

# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'
