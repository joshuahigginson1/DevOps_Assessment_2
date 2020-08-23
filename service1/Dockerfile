FROM fnndsc/ubuntu-python3:18.04

LABEL version="1.0"
LABEL description="Melodie - Service 1 Container."

EXPOSE 5001

WORKDIR /

COPY . .

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip
RUN pip3 install -r s1_requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "service1_wsgi.py"]