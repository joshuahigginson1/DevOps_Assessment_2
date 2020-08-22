FROM python:3.8-buster

LABEL version="1.0"
LABEL description="Melodie - Service 3 Container."

EXPOSE 5003

WORKDIR /

COPY . .

RUN sudo apt-get update && sudo apt-get -y upgrade
RUN apt-get install -y python3 python3-pip
RUN pip3 install -r s3_requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "service3_wsgi.py"]