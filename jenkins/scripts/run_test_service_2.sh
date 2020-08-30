#!/bin/sh

cd service2/src

sudo chmod -R 777 tests

cd tests

export FLASK_ENV="$FLASK_ENV"

sudo rm test_results/*

python3 -m pytest -v --cov=src --cov-report term-missing xml:test_cov_service1.xml --junit-xml=test_results/test_results_service2.xml

printf "\n"
printf "\n"
printf "\n"

# Run our PyLint function, and save the output to a new .log file.
# Pylint returns a non-zero exit code, even only if a small warning issue
# was found. This will cause our builds to fail.

# So instead, we use the 'pylint-fail-under' plugin.

echo 'Writing PYLINT Report...'

sudo pylint-fail-under --load-plugins='pylint_flask','pylint_flask_sqlalchemy' --fail_under 1 -f parseable src > test_results/service2_pylint_report.log

# Run our Pep8 function, and saves the output to a new .txt file.
# We just want the style report, not for the program to fail our build.

echo 'Writing PEP8 Report...'

sudo pycodestyle /var/lib/jenkins/workspace/melodie-pipeline/service2/src > test_results/service2_pep8_report.txt || exit 0