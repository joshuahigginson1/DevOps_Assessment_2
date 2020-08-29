FROM python:3.8.5-buster

LABEL version="1.0"
LABEL description="Melodie - Service 3 Container."

EXPOSE 5003

WORKDIR /

COPY . .

RUN apt update && apt -y upgrade
RUN apt install gunicorn -y
RUN pip3 install -r s3_requirements.txt

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]