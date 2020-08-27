#!/bin/sh

# This script will install ansible on an ubuntu machine.

sudo apt update

sudo apt upgrade -y

sudo apt install -y software-properties-common

sudo apt-add-repository -y --update ppa:ansible/ansible

sudo apt install -y ansible