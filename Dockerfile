FROM python:3.11.7-slim
LABEL maintainer="Eric"

USER root

# 设置环境变量
ENV TZ=Asia/Shanghai \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=zh_CN.UTF-8

ARG VERSION=1.0.0

RUN set -eux && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime && \
    rm -rf /etc/apt/sources.list.d/debian.sources && touch /etc/apt/sources.list && \ 
    echo "deb https://mirrors.aliyun.com/debian/ bookworm main contrib non-free non-free-firmware" > /etc/apt/sources.list && \
    echo "deb https://mirrors.aliyun.com/debian/ bookworm-updates main contrib non-free non-free-firmware" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.aliyun.com/debian/ bookworm-backports main contrib non-free non-free-firmware" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.aliyun.com/debian-security bookworm-security main contrib non-free non-free-firmware" >> /etc/apt/sources.list && \
    apt update && apt install -y iptables iproute2 procps vim && pip install -U pip


RUN pip install requests lxml flask jinja2 gevent  --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple && apt clean && rm -rf /var/lib/apt/lists/* 

COPY ./weibo.py /opt/weibo/

WORKDIR /opt/weibo

EXPOSE 5000
ENTRYPOINT ["python","weibo.py"]
