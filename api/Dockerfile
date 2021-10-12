FROM python:3.8-slim

WORKDIR /src
COPY ./config .
RUN pip3 install -r requirements.txt --no-cache-dir



RUN chmod +x wait-for-it.sh
RUN chmod +x runserver.sh