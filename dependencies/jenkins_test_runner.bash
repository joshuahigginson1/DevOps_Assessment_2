# A bash script in order to run my test dependencies.

# Fix for "pyenv not working" error, caused by locales.

export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales

# Update dependencies.
sudo ap-get update
sudo apt-get install -y python3 python3-pip python3-venv

# Create our virtual environment.
python3 -m venv venv

# Activate our virtual environment.
source /venv/bin/activate

# Install our project requirements.
sudo pip3 install -r dependencies/requirements.txt

# Run our test suite.
pytest --junit-xml=src/tests.test_results/results.xml