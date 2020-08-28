#!/bin/sh

cd service3/src/tests

sudo pytest --junit-xml=test_results/test_results_service3.xml

printf "\n"
printf "\n"
printf "\n"

# Run our PyLint function, and save the output to a new .log file.
# Pylint returns a non-zero exit code, even only if a small warning issue
# was found. This will cause our builds to fail.

# So instead, we use the 'pylint-fail-under' plugin.

sudo sh -c "pylint-fail-under --fail_under 1 -f parseable src > test_results/service3_pylint_report.log"

# Run our Pep8 function, and saves the output to a new .txt file.
# We just want the style report, not for the program to fail our build.

sudo sh -c "pycodestyle src > test_results/service3_pep8_report.txt || exit 0"