#syntax=docker/dockerfile:1
FROM python:3.10.0a6-alpine3.13
WORKDIR /CveVxworks/
RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN scrapy crawl Cve
CMD ["python","display.py"]
