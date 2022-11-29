FROM python:3.11.0-slim-bullseye AS buildprep

RUN apt-get update && \
#apt-get install -y python3 python3-pip python3-venv
apt-get install -y gcc

RUN python3 -m venv /tmp/prometheus_client/venv
COPY requirements.txt /tmp/prometheus_client/
RUN . /tmp/prometheus_client/venv/bin/activate && \
pip --disable-pip-version-check --cache-dir /tmp/prometheus_client/venv install -r /tmp/prometheus_client/requirements.txt

RUN apt-get autoremove -y && apt-get clean

COPY shtc3_sensor_prom.py /tmp/prometheus_client/main.py

FROM python:3.11.0-slim-bullseye
LABEL MAINTAINER="lonkaut@gmail.com"

COPY --from=buildprep /tmp/prometheus_client /tmp/prometheus_client


CMD . /tmp/prometheus_client/venv/bin/activate && exec python3 -u /tmp/prometheus_client/main.py
