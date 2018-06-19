FROM gliderlabs/alpine:3.3

RUN mkdir -p /opt/microservice

ADD . /opt/microservice

RUN apk --update add python py-pip openssl ca-certificates

RUN pip install -r requirements.txt

EXPOSE 5000

WORKDIR /opt/microservice

CMD [ "python app.py" ]