# A bash script in order to run my test dependencies.

# Here, I declare my paths.
code_path=./src
venv_path=./venv
test_dir=/src/tests
test_results_dir=./src/tests/test_results

# Activate our virtual environment.
#
# source venv/bin/activate

# Install our project requirements.
sudo pip3 install -r ./dependencies/requirements.txt

# Run our test suite.
pytest --junit-xml=${test_results_dir}/results.xml