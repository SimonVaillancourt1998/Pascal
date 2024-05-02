FROM python:3.11-slim

COPY main /
COPY responses.py /
COPY requirements.txt /
COPY .env /
RUN pip install -r requirements.txt

WORKDIR /

SHELL [ "/main" ]