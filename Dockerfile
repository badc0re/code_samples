FROM python:3.7-slim

RUN apt update && apt install -y -q --no-install-recommends \
    wget \
    ca-certificates \
    curl

# get pip
RUN wget https://bootstrap.pypa.io/get-pip.py \
    && python get-pip.py \
    && pip install --upgrade pip

WORKDIR /app
ADD . /app
RUN pip install .
