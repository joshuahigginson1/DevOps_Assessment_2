#!/bin/bash

# This script will install ansible on an ubuntu machine.

sudo apt update

sudo apt install software-properties-common

sudo apt-add-repository -y --update ppa:ansible/ansible

sudo apt install ansible