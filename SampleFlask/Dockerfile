FROM python:3.5.2-slim

RUN apt-get update && apt-get install -y gcc unixodbc-dev

RUN mkdir -p /opt/microservice

ADD . /opt/microservice

WORKDIR /opt/microservice

RUN pip install -r requirements.txt

EXPOSE 5000


CMD [ "python", "app.py" ]
