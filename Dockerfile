# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.4

FROM python:${PYTHON_VERSION}-bookworm

# create a non-privileged user and group to build the script bundle
RUN groupadd -g 1001 automation && \
        useradd -m -u 1001 -g automation -s /bin/bash agent

WORKDIR /home/agent/html-renderer

# activate a virtual python environment
RUN python -m venv venv && \
        . ./venv/bin/activate

COPY --chown=agent:automation requirements.txt requirements.txt

RUN pip install --upgrade pip && \
        pip install --no-cache-dir pyinstaller && \
        pip install --no-cache-dir -r requirements.txt

# install OS browser dependencies and chromium binaries
RUN PLAYWRIGHT_BROWSERS_PATH=0 playwright install --with-deps chromium

COPY src src

# build the script bundle with chromium binaries
RUN pyinstaller -n render-html -F ./src/__main__.py && \
        cp ./dist/render-html /usr/local/bin/render-html

# create non-privelleged user to run the script
RUN useradd -m -u 1002 -g automation -s /bin/bash headless

WORKDIR /home/headless

USER headless


