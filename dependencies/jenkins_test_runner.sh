# A bash script in order to run my test dependencies.

# Update dependencies.
sudo apt update
sudo apt install -y python3 python3-pip python3-venv

# Create our virtual environment.
python3 -m venv venv

# Activate our virtual environment.
source /venv/bin/activate

# Install our project requirements.
sudo pip3 install -r dependencies/requirements.txt

# Run our test suite.
sudo pytest --junit-xml=src/tests/test_results/junit_results.xml

# Run our PyLint function, and save the output to a new .log file. Have to run this in it's own subshell.
# Pylint returns a non-zero exit code even only if a small warning issue was found. This will cause our builds to fail.
# This is why se use the 'pylint-fail-under' plugin.

printf "\n"
printf "\n"
printf "\n"

sudo bash -c "pylint-fail-under --fail_under 1 -f parseable src > src/tests/test_results/pylint.log"

# Run our Pep8 function, and saves the output to a new .xml file.
sudo bash -c "pep8 src > src/tests/test_results/pep8.log"