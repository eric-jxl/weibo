# weibo
### The Weibo Hot List

[![Docker Image CI](https://github.com/eric-jxl/weibo/actions/workflows/docker-image.yml/badge.svg)](https://github.com/eric-jxl/weibo/actions/workflows/docker-image.yml)
[![Sonarcloud Build](https://github.com/eric-jxl/weibo/actions/workflows/build.yml/badge.svg)](https://github.com/eric-jxl/weibo/actions/workflows/build.yml)
### 针对ghcr.io 打包镜像
- 使用[Github Actions](.github/workflows/docker-image.yml) 自动打包Docker镜像发布到[ghcr.io](https://github.com/eric-jxl/weibo/pkgs/container/weibo)
- 使用[Sonar](.github/workflows/build.ym)代码漏洞检查

> - *仅修改py文件和Dockerfile 触发CI/CD 打包镜像*
> - *提交PR 触发自动代码检查*
