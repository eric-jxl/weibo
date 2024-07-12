FROM python:3.11.7-slim
LABEL maintainer="Eric"
LABEL org.opencontainers.image.source = "https://github.com/eric-jxl/weibo"

USER root

# 设置环境变量
ENV TZ=Asia/Shanghai \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=zh_CN.UTF-8


RUN set -eux && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime && \
    apt update && apt install -y iptables iproute2 procps vim && pip install -U pip


RUN pip install requests lxml flask jinja2 gevent --user --no-cache-dir  && apt clean && rm -rf /var/lib/apt/lists/* 

COPY ./weibo.py /opt/weibo/

WORKDIR /opt/weibo

EXPOSE 5000
ENTRYPOINT ["python","weibo.py"]
