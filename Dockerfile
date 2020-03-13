FROM python:3.7
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

RUN pip install pyzbar[scripts]

RUN mkdir /app
WORKDIR /app
COPY ./app /app

