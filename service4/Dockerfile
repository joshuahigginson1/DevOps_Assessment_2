FROM python:3.8-buster

LABEL version="1.0"
LABEL description="Melodie - Service 4 Container."

EXPOSE 5004

WORKDIR /

COPY . .

RUN sudo apt-get update && sudo apt-get upgrade
RUN sudo apt-get install python3 python3-pip
RUN pip3 install -r s4_requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "service4_wsgi.py"]