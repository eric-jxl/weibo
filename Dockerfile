FROM python:3.11.7-slim
LABEL maintainer="Eric"
LABEL org.opencontainers.image.source="https://github.com/eric-jxl/weibo"

USER root

WORKDIR /opt/weibo

# 设置环境变量
ENV TZ=Asia/Shanghai \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 


RUN set -eu && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime && \
    apt update && apt install -y iptables iproute2 procps vim


RUN pip install -U pip && pip install requests lxml flask jinja2 gevent --user --no-cache-dir  && apt clean && rm -rf /var/lib/apt/lists/* 

COPY weibo.py /opt/weibo/
COPY config.py /opt/weibo/
COPY run.sh /opt/weibo/


EXPOSE 5000
ENTRYPOINT ["./run.sh"]
