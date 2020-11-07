FROM python:3.8

ENV PYTHONBUFFERED=1

RUN mkdir ./commercial_store

WORKDIR /commercial_store

ADD . /commercial_store

ADD . /commercial_store/

RUN pip install -r requirements.txt