#!/bin/sh

pwd

cd service4/src/tests

sudo pytest --junit-xml=service4/src/tests/test_results/junit_results.xml

printf "\n"
printf "\n"
printf "\n"

# Run our PyLint function, and save the output to a new .log file.
# Pylint returns a non-zero exit code, even only if a small warning issue
# was found. This will cause our builds to fail.

# So instead, we use the 'pylint-fail-under' plugin.

sh -c "pylint-fail-under --fail_under 1 -f parseable src > src/tests/test_results/pylint_report.log"

# Run our Pep8 function, and saves the output to a new .txt file.
# We just want the style report, not for the program to fail our build.

sh -c "pycodestyle src > src/tests/test_results/pep8_report.txt || exit 0"