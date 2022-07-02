FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt
COPY ./app /app
COPY ./entrypoint.sh /entrypoint.sh

RUN pip install -r /requirements.txt

WORKDIR /app

ENTRYPOINT [ "sh", "/entrypoint.sh" ]
