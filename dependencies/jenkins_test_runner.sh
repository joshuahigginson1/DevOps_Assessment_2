# A bash script in order to run my test dependencies.

# Update dependencies.
sudo apt update
sudo apt install -y python3

python --version

sudo apt install -y python3-pip

pip3 --version

sudo apt install -y python3-venv

# Create our virtual environment.
python3 -m venv venv

# Activate our virtual environment.
source /venv/bin/activate

# Install our project requirements.
cat dependencies/requirements.txt
sudo pip3 install -r dependencies/requirements.txt

# Run our test suite.
pytest --junit-xml=src/tests.test_results/results.xml