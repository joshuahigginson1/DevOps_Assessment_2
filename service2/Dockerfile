FROM python:3.8-buster

LABEL version="1.0"
LABEL description="Melodie - Service 2 Container."

EXPOSE 5002

WORKDIR /

COPY . .

RUN sudo apt-get update && sudo apt-get upgrade
RUN sudo apt-get install python3 python3-pip
RUN pip3 install -r s2_requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "service2_wsgi.py"]