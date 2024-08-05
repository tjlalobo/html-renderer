# syntax=docker/dockerfile:1

FROM mcr.microsoft.com/playwright/python:v1.45.0-jammy

USER pwuser

WORKDIR /home/pwuser/scripts

COPY --chown=pwuser:pwuser requirements.txt requirements.txt

RUN pip install --upgrade pip && \
        pip install --no-cache-dir -r requirements.txt

COPY --chown=pwuser:pwuser render-html render-html

