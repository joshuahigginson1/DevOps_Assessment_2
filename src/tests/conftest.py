# Conftest.py is used to share PyTest Fixtures across multiple test files.

# Although conftest.py is a Python module, don’t import conftest into our test files.

# “The conftest.py file gets read by pytest, and is considered a local plugin.

# Imports ---------------------------------------------------------------------------------

import pytest

# Fixtures --------------------------------------------------------------------------------

"""@pytest.fixture(name="connect_database", scope='module', autouse=False)
def tasks_db_connection(tmpdir):
        #tasks_db connects to our db before testing, then disconnects straight after.
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()"""


# Fixtures are a great place to store data to use for testing. You can return anything.


@pytest.fixture(name='common_scales', scope='function', autouse=False)
def common_scales():  # All of the common scales. In tab, this would be all scales with the root note of 'F'.
    common_scales = {
        "chromatic": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "major": [1, 3, 5, 6, 8, 10, 12, 13],
        "major pentatonic": [1, 3, 5, 8, 10, 13],
        "major blues": [1, 3, 4, 5, 8, 10, 13],
        "natural minor": [1, 3, 4, 6, 8, 9, 11, 13],
        "harmonic minor": [1, 3, 4, 6, 8, 9, 12, 13],
        "minor pentatonic": [1, 4, 6, 8, 11, 13],
        "minor blues": [1, 4, 6, 7, 8, 11, 13]
    }
    return common_scales


@pytest.fixture(name='all_rhythms', scope='function', autouse=False)
def lilypond_rhythms():  # Every rhythm that Lilypond accepts.
    return ["longa", "breve", 1, 2, 4, 8, 16, 32, 64, 128]  # All standard variations of pitch in Lilypond.


@pytest.fixture(name='common_rhythms', scope='function', autouse=False)
def common_rhythms():  # All common rhythms, and subsets of rhythm.
    common_rhythms = {
        "short": [8, 16, 32, 64],
        "long": [1, 2, 4],
        "standard": [1, 2, 4, 8, 16, 32],
        "extremes": ["longa", "breve", 64, 128]
    }
    return common_rhythms

