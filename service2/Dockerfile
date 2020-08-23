FROM python:3.8.5-buster

LABEL version="1.0"
LABEL description="Melodie - Service 2 Container."

EXPOSE 5002

WORKDIR /

COPY . .

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip
RUN pip3 install -r s2_requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "service2_wsgi.py"]