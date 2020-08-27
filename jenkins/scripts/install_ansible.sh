#!/bin/sh

# This script will install ansible on an ubuntu machine.

apt update

apt install software-properties-common

apt-add-repository -y --update ppa:ansible/ansible

apt install ansible