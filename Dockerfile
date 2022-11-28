FROM python:3.11-alpine AS buildprep

RUN apk update && \
apk add gcc


FROM buildprep
USER nobody
LABEL MAINTAINER="lonkaut@gmail.com"

RUN python3 -m venv /tmp/prometheus_client/venv
RUN python3 -m venv /tmp/prometheus_client/venv

COPY requirements.txt /tmp/prometheus_client/
RUN . /tmp/prometheus_client/venv/bin/activate && \
pip --disable-pip-version-check --cache-dir /tmp/prometheus_client/venv install -r /tmp/prometheus_client/requirements.txt

COPY shtc3_sensor_prom.py /tmp/prometheus_client/main.py

CMD modprobe i2c-dev && . /tmp/prometheus_client/venv/bin/activate && exec python3 -u /tmp/prometheus_client/main.py