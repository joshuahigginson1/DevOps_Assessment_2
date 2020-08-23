FROM joshuahigginson1/ubuntu-lilypond:python-3.8.5

LABEL version="1.0"
LABEL description="Melodie - Service 4 Container."

EXPOSE 5004

WORKDIR /

COPY . .

RUN apt-get update && apt-get -y upgrade
RUN pip3 install -r s4_requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "service4_wsgi.py"]