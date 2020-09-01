"""Conftest.py is used to share PyTest Fixtures across multiple test files.

Don’t import conftest into our test files.

The conftest.py file gets read by pytest, and is considered a local plugin.
"""

# Imports --------------------------------------------------------------

import pytest

# Fixtures -------------------------------------------------------------

# Fixtures are a great place to store data to use for testing.
# You can return anything.


@pytest.fixture(name='all_rhythms', scope='function', autouse=False)
def mingus_rhythms():
    """A fixture which only returns the standard variations of pitch in
    mingus convention."""

    return [0.25, 0.5, 1, 2, 4, 8, 16, 32, 64, 128]


@pytest.fixture(name='common_rhythms', scope='function', autouse=False)
def common_rhythms():
    """A fixture to test all subsets of common musical rhythm."""

    common_rhythms_dictionary = {
        "short": [4, 8, 16, 32],
        "long": [1, 2, 4],
        "standard": [2, 4, 8, 16],
        "extremes": [1, 32, 64, 128],
        "midi implementation": [2, 4, 8, 16]
    }

    return common_rhythms_dictionary
