# Will be running these tests on the jenkins machine.

# Git Repo gets pulled down from our github account.

# Need to install all of the requirements to run python3.8, pytest, etc.

scp docker-compose.yaml jenkins@melodie-manager-1:/home/jenkins

ssh -t jenkins@melodie-manager-1 << EOF

echo "This machine is currently being controlled by Jenkins-Ansible-Driver."

docker login -u"$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"

export FLASK_ENV=$FLASK_ENV

export TESTING_SECRET_KEY="$TESTING_SECRET_KEY"
export DEV_SECRET_KEY="$DEV_SECRET_KEY"
export PRODUCTION_SECRET_KEY="$PRODUCTION_SECRET_KEY"

export FILES_DIRECTORY="$FILES_DIRECTORY"
export PNG_DIRECTORY="$PNG_DIRECTORY"
export MIDI_DIRECTORY="$MIDI_DIRECTORY"

export PRODUCTION_DB="$PRODUCTION_DB"
export PRODUCTION_DB_USERNAME="$PRODUCTION_DB_USERNAME"
export PRODUCTION_DB_USERPASS="$PRODUCTION_DB_USERPASS"
export PRODUCTION_DATABASE_ADDRESS="$PRODUCTION_DATABASE_ADDRESS"

export DEVELOPMENT_DB="$DEVELOPMENT_DB"
export DEVELOPMENT_DB_USERNAME="$DEVELOPMENT_DB_USERNAME"
export DEVELOPMENT_DB_USERPASS="$DEVELOPMENT_DB_USERPASS"
export DEVELOPMENT_DATABASE_ADDRESS="$DEVELOPMENT_DATABASE_ADDRESS"

export TESTING_DB="$TESTING_DB"
export TESTING_DB_USERNAME="$TESTING_DB_USERNAME"
export TESTING_DB_USERPASS="$TESTING_DB_USERPASS"
export TESTING_DATABASE_ADDRESS="$TESTING_DATABASE_ADDRESS"

export SERVICE_1_URL="$SERVICE_1_URL"
export SERVICE_2_URL="$SERVICE_2_URL"
export SERVICE_3_URL="$SERVICE_3_URL"
export SERVICE_4_URL="$SERVICE_4_URL"

docker stack deploy --with-registry-auth -c docker-compose.yaml melodie-stack

EOF
