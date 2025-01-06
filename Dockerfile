FROM python:latest
RUN apt-get -y update
RUN apt-get install -y apt-transport-https ca-certificates curl gnupg git-all gh
COPY requirements.txt .
RUN pip3 install -r requirements.txt