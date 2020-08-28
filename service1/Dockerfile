FROM python:3.8.5-buster

LABEL version="1.0"
LABEL description="Melodie - Service 1 Container."

EXPOSE 5001

WORKDIR /

COPY . .

RUN apt update && apt upgrade -y
RUN apt install gunicorn -y
RUN pip3 install -r s1_requirements.txt

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]