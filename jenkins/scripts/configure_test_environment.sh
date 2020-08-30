#!/bin/sh

# A script to configure our test environment.

# Update dependencies.
sudo apt update
sudo apt upgrade -y
# sudo apt install -y python3 python3-pip python3-venv lilypond gunicorn

# Create our virtual environment.
# sudo python3 -m venv venv

# Activate our virtual environment.
# source /var/lib/jenkins/workspace/melodie-pipeline/venv/bin/activate

# Install our project requirements.
sudo pip3 install -r jenkins/test_env/test_env_requirements.txt