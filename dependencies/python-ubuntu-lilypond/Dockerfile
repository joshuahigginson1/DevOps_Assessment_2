FROM ubuntu:18.04

MAINTAINER joshuahigginson1 "joshuahigginson1@gmail.com"

RUN apt-get update && apt-get upgrade
RUN apt-get install -y python3.8 python3-pip lilypond
RUN cd /usr/local/bin && ln -s /usr/bin/python3 python
RUN pip3 install --upgrade pip

ENTRYPOINT ["/usr/local/bin", "python3"]