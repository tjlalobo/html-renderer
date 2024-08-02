# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.4

FROM python:${PYTHON_VERSION}-bookworm AS base

# create a non-privileged user that the app will run under.
RUN groupadd -g 1001 airflow && \
        useradd -m -u 1001 -g airflow -s /bin/bash crawler

WORKDIR /home/crawler

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && \
        python -m pip install -r requirements.txt

# install browser OS-dependencies
RUN playwright install-deps

# switch to non-priveliged used to install chromium binary and run the script
USER crawler

# install chromium binaries in non-root user local cache
RUN playwright install chromium

# copy source code into the container
COPY ./app ./app

# run the script
CMD [ "python", "./app"]