FROM python:3.7-alpine

LABEL Author="Oumayma Lakrari"
LABEL E-mail="olakrari@gmail.com"
LABEL Version="db : MySQL ; cache memory : Redis ; backend : Flask v0.1"

RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev 

WORKDIR /backend
COPY . /backend

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT python run.py