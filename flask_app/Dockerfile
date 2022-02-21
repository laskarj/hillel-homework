# syntax=docker/dockerfile:1
FROM ubuntu:20.04
MAINTAINER Eduard Laskarjevsky "laskarjevsky.eduard@gmail.com"
RUN apt-get update -y
RUN apt install -y python3.8
RUN apt-get install -y python3-pip python3-dev
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ADD ./flask_application.py ./flask_application.py
CMD ["python3", "./flask_application.py"]
