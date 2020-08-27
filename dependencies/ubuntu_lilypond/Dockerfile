# FROM ubuntu:18.04
FROM python:3.8.5-buster

LABEL "Debian Version: "="Debian Buster"
LABEL "Lilypond Version: "="Lilypond 2.20.0-1 Stable"

MAINTAINER joshuahigginson1 joshuahigginson1@gmail.com

RUN apt-get update \
    && apt-get install --yes bzip2

ADD https://lilypond.org/download/binaries/linux-64/lilypond-2.20.0-1.linux-64.sh ./

RUN sh lilypond-2.20.0-1.linux-64.sh --batch --prefix /usr/local \
    && rm lilypond-2.20.0-1.linux-64.sh

RUN apt-get remove --purge --yes bzip2 \
    && apt-get clean \
    && apt-get autoclean