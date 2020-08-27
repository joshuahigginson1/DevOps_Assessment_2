#!/bin/sh

# A script to configure our test environment.

# Update dependencies.
apt update
apt upgrade
apt install -y python3 python3-pip python3-venv lilypond gunicorn

# Create our virtual environment.
python3 -m venv venv

# Activate our virtual environment.
source /venv/bin/activate

# Install our project requirements.
pip3 install -r jenkins/test_env/test_env_requirements.txt
