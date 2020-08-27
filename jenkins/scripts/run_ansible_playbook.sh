#!/bin/bash

# This script will run our ansible playbook to provision a production env.

cd ~/DevOps_Assessment_2/ansible

sudo ansible-playbook -i inventory.ini playbook.yaml