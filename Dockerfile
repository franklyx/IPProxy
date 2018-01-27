FROM python:latest

MAINTAINER YuexLi
# 安装supervisor
RUN apt-get update \
    && apt-get install -y supervisor

RUN rm /etc/supervisor/supervisord.conf
COPY doc/supervisord.conf /etc/supervisor/supervisord.conf
COPY doc/proxy.conf /etc/supervisor/conf.d/proxy.conf

# 设置工作目录
RUN mkdir -p /home/code
WORKDIR /home/code

# 添加应用
ADD . /home/code

# 添加以及安装依赖
COPY doc/requirements.txt /home/code/requirements.txt
RUN pip install -r requirements.txt

# 启动supervisor
COPY doc/start_supervisor.sh /home/code/start_supervisor.sh
CMD ["sh","start_supervisor.sh"]