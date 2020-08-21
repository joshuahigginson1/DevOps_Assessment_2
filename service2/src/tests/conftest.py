"""Conftest.py is used to share PyTest Fixtures across multiple test files.

Don’t import conftest into our test files.

The conftest.py file gets read by pytest, and is considered a local plugin.

"""

# Imports --------------------------------------------------------------

import pytest


# Fixtures -------------------------------------------------------------

# Fixtures are a great place to store data to use for testing.
# You can return anything.


@pytest.fixture(name='all_pitches', scope='function', autouse=False)
def melodie_proprietary_pitches():
    """A fixture which returns the notes in a chromatic musical scale,
    into our own proprietary format."""

    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "r"]


@pytest.fixture(name='common_scales', scope='function', autouse=False)
def common_scales():
    """A fixture which returns all of the common musical scales,
    in mélodies' own proprietary format.

    Represented in musical tab, this would be all of the scales in which
    the root note starts with 'F'.
    """
    common_scales = {
        "chromatic": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "r"],
        "major": [1, 3, 5, 6, 8, 10, 12, "r"],
        "major pentatonic": [1, 3, 5, 8, 10, "r"],
        "major blues": [1, 3, 4, 5, 8, 10, "r"],
        "natural minor": [1, 3, 4, 6, 8, 9, 11, "r"],
        "harmonic minor": [1, 3, 4, 6, 8, 9, 12, "r"],
        "minor pentatonic": [1, 4, 6, 8, 11, "r"],
        "minor blues": [1, 4, 6, 7, 8, 11, "r"]
    }
    return common_scales


@pytest.fixture(name='note_names_in_c', scope='function', autouse=False)
def note_names_in_c():

    c_chromatic_dictionary = {
        1: 'C',
        2: 'C#',
        3: 'D',
        4: 'D#',
        5: 'E',
        6: 'F',
        7: 'F#',
        8: 'G',
        9: 'G#',
        10: 'A',
        11: 'A#',
        12: 'B',
        "r": "r"
    }

    return c_chromatic_dictionary
