# Melodie Jenkins Pipeline
# A script to configure our test environment.

# Update dependencies.
sudo apt update
sudo apt install -y python3 python3-pip python3-venv lilypond

# Create our virtual environment.
python3 -m venv venv

# Activate our virtual environment.
source /venv/bin/activate

# Install our project requirements.
sudo pip3 install -r dependencies/requirements.txt
