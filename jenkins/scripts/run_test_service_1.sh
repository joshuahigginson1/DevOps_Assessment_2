#!/bin/sh

cd service1/src

sudo chmod -R 777 tests

cd tests

export FLASK_ENV="$FLASK_ENV"

export TESTING_SECRET_KEY="$TESTING_SECRET_KEY"

export FILES_DIRECTORY="$FILES_DIRECTORY"

export TESTING_DB="$TESTING_DB"
export TESTING_DB_USERNAME="$TESTING_DB_USERNAME"
export TESTING_DB_USERPASS="$TESTING_DB_USERPASS"
export TESTING_DATABASE_ADDRESS="$TESTING_DATABASE_ADDRESS"

sudo rm test_results/*

python3 -m pytest -v --cov=src --cov-report xml:test_results/test_cov_service1.xml --junit-xml=test_results/test_results_service1.xml

printf "\n"
printf "\n"
printf "\n"

# Run our PyLint function, and save the output to a new .log file.
# Pylint returns a non-zero exit code, even only if a small warning issue
# was found. This will cause our builds to fail.

# So instead, we use the 'pylint-fail-under' plugin.

echo 'Writing PYLINT Report...'

sudo pylint-fail-under --load-plugins='pylint_flask','pylint_flask_sqlalchemy' --fail_under 1 -f parseable src > test_results/service1_pylint_report.log

# Run our Pep8 function, and saves the output to a new .txt file.
# We just want the style report, not for the program to fail our build.

echo 'Writing PEP8 Report...'

sudo pycodestyle /var/lib/jenkins/workspace/melodie-pipeline/service1/src > test_results/service1_pep8_report.txt || exit 0
