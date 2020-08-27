FROM joshuahigginson1/ubuntu-lilypond:2.20.0-1

LABEL "Ubuntu Version: "="Ubuntu 18-04"
LABEL "Lilypond Version: "="Lilypond 2.20.0-1 Stable"
LABEL "Python Version: "="Python 3.8.5"

# Stops annoying error messages.
ENV DEBIAN_FRONTEND noninteractive

# Update the package manager.
RUN apt-get update

# Install Python3.8
RUN apt-get install python3.8

# Ensure that python is installed in the local path.

ENV PATH /usr/local/bin:$PATH

RUN apt-get update && apt-get -y upgrade

RUN apt-get install

ENTRYPOINT ["python3.8"]