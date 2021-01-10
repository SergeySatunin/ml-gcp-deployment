FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python

COPY flask_service.py flask_service.py
COPY requirements.txt requirements.txt
COPY model.pkl model.pkl

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "flask_service.py"]