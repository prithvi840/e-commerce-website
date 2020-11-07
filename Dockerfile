FROM python:3.8

ENV PYTHONBUFFERED=1

RUN mkdir ./commercial_store

WORKDIR /commercial_store

COPY requirements.txt /commercial_store/

RUN pip install -r requirements.txt

COPY . /commercial_store/