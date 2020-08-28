# Will be running these tests on the jenkins machine.

# Git Repo gets pulled down from our github account.

# Need to install all of the requirements to run python3.8, pytest, etc.

scp docker-compose.yaml jenkins@melodie-manager-1:/home/jenkins

ssh jenkins@melodie-manager-1 << EOF
echo "This machine is currently being controlled by Jenkins-Ansible-Driver."
ls
docker stack deploy --compose-file docker-compose.yaml melodie-stack
EOF

