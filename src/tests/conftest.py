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

    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, "r"]


@pytest.fixture(name='common_scales', scope='function', autouse=False)
def common_scales():
    """A fixture which returns all of the common musical scales,
    in mélodies' own proprietary format.

    Represented in musical tab, this would be all of the scales in which
    the root note starts with 'F'.
    """
    common_scales = {
        "chromatic": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, "r"],
        "major": [1, 3, 5, 6, 8, 10, 12, 13, "r"],
        "major pentatonic": [1, 3, 5, 8, 10, 13, "r"],
        "major blues": [1, 3, 4, 5, 8, 10, 13, "r"],
        "natural minor": [1, 3, 4, 6, 8, 9, 11, 13, "r"],
        "harmonic minor": [1, 3, 4, 6, 8, 9, 12, 13, "r"],
        "minor pentatonic": [1, 4, 6, 8, 11, 13, "r"],
        "minor blues": [1, 4, 6, 7, 8, 11, 13, "r"]
    }
    return common_scales


@pytest.fixture(name='all_rhythms', scope='function', autouse=False)
def mingus_rhythms():
    """A fixture which only returns the standard variations of pitch in
    mingus convention."""

    return [0.25, 0.5, 1, 2, 4, 8, 16, 32, 64, 128]


@pytest.fixture(name='common_rhythms', scope='function', autouse=False)
def common_rhythms():
    """A fixture to test all subsets of common musical rhythm."""

    common_rhythms_dictionary = {
        "short": [8, 16, 32, 64],
        "long": [1, 2, 4],
        "standard": [1, 2, 4, 8, 16, 32],
        "extremes": [0.25, 0.5, 64, 128]
    }
    return common_rhythms_dictionary


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


# Depreciated Fixtures -------------------------------------------------

@pytest.fixture(name='key_offset_dict', scope='function', autouse=False)
def key_offset():
    """A fixture which returns the key offset values for every musical key,
    in relation to F. Returns values as key-value pairs.

    NB: A musical sharp is denoted by the suffix 'is'.
    NB: A flat pitch is denoted by the suffix 'es'.
    """

    key_offset_dictionary = {
        'C': 0,
        'C#': 1,
        'Db': 1,
        'D': 2,
        'D#': 3,
        'Eb': 3,
        'E': 4,
        'F': 5,
        'F#': 6,
        'Gb': 6,
        'G': 7,
        'G#': 8,
        'Ab': 8,
        'A': 9,
        'A#': 10,
        'Bb': 10,
        'B': 11
    }

    return key_offset_dictionary


@pytest.fixture(name='all_keys', scope='function', autouse=False)
def all_lilypond_keys():
    """A list of every possible music key root."""
    return ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb',
            'G', 'A#', 'Ab', 'A', 'A#', 'Bb', 'B']
