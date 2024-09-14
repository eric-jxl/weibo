#!/usr/bin/env python3

import multiprocessing
import os
import gevent.monkey
gevent.monkey.patch_all()


# debug = True
bind = "0.0.0.0:5000"
timeout = 30

loglevel = 'info'
daemon = False
preload_app = True
pidfile = '/var/run/gunicorn.pid'


workers = multiprocessing.cpu_count() # 启动的进程数
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'
