FROM python:3.8.5-buster

LABEL version="1.0"
LABEL description="Melodie - Service 2 Container."

EXPOSE 5002

WORKDIR /

COPY . .

RUN apt update && apt -y upgrade
RUN apt install gunicorn -y
RUN pip3 install -r s2_requirements.txt

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
