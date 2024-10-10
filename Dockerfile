FROM python:3.12

WORKDIR /app

ADD . /app/

COPY requirements.txt /app/

RUN apt-get update

RUN pip install -r requirements.txt

COPY . .

RUN pytest -v