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
sudo sh -c "pylint -f parseable src > src/tests/test_results/pylint.log"