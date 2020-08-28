# Will be running these tests on the jenkins machine.

# Git Repo gets pulled down from our github account.

# Need to install all of the requirements to run python3.8, pytest, etc.

scp docker-compose.yaml jenkins@melodie-manager-1:/home/jenkins

ssh -t jenkins@melodie-manager-1 << EOF

echo "This machine is currently being controlled by Jenkins-Ansible-Driver."

docker login -u"$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"

printenv

docker stack deploy --with-registry-auth -c docker-compose.yaml melodie-stack

EOF
