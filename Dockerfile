FROM py-ubuntu:3.11

MAINTAINER haoxingwei@eastmoney.com

# RUN apt update -y
# RUN apt install -y --no-install-recommends wget curl vim nginx python3.11 ca-certificates supervisor pkg-config build-essential libmysqlclient-dev python3.11-dev

RUN mkdir -p /data/apps/rtc_ai /data/logs
WORKDIR /data/apps/rtc_ai
COPY . /data/apps/rtc_ai

RUN curl -k -s -O https://bootstrap.pypa.io/get-pip.py && python3.11 get-pip.py
RUN export PATH=/usr/include/python3.11:$PATH && python3.11 -m pip install -r requirements.txt
RUN python3.11 manage.py collectstatic --no-input

COPY scripts/nginx.conf /etc/nginx/nginx.conf

COPY scripts/supervisor-main.conf /etc/supervisord.conf

EXPOSE 9000

ENTRYPOINT ["/usr/bin/supervisord"]