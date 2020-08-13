# Conftest.py is used to share PyTest Fixtures across multiple test files.

# Although conftest.py is a Python module, don’t import conftest into our test files.

# “The conftest.py file gets read by pytest, and is considered a local plugin.

# Fixtures --------------------------------------------------------------------------------

"""@pytest.fixture(name="connect_database", scope='module', autouse=False)
def tasks_db_connection(tmpdir):
        #tasks_db connects to our db before testing, then disconnects straight after.
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()"""
