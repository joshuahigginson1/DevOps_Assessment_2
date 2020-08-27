#!/bin/sh

# This script will run our ansible playbook to provision a production env.

cd ~/DevOps_Assessment_2/ansible

ansible-playbook -i inventory.ini playbook.yaml