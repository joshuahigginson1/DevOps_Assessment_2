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
def lilypond_rhythms():
    """A fixture which only returns the standard variations of pitch in
    Lilypond convention."""

    return ["longa", "breve", 1, 2, 4, 8, 16, 32, 64, 128]


@pytest.fixture(name='common_rhythms', scope='function', autouse=False)
def common_rhythms():
    """A fixture to test all subsets of common musical rhythm."""

    common_rhythms = {
        "short": [8, 16, 32, 64],
        "long": [1, 2, 4],
        "standard": [1, 2, 4, 8, 16, 32],
        "extremes": ["longa", "breve", 64, 128]
    }
    return common_rhythms
