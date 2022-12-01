#syntax=docker/dockerfile:1
FROM python:3.11-alpine3.16
EXPOSE 80
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
RUN python3 ./go-spider.py
CMD ["python","display.py"]
