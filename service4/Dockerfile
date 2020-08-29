FROM joshuahigginson1/ubuntu-lilypond:python-3.8.5

LABEL version="1.0"
LABEL description="Melodie - Service 4 Container."

EXPOSE 5004

WORKDIR /

COPY . .

RUN apt update && apt -y upgrade
RUN apt install gunicorn -y
RUN pip3 install -r s4_requirements.txt

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]