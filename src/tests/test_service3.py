"""This file contains the functions for service2 Implementation 1 & 2."""

# Imports --------------------------------------------------------------

from src.service3.service3 import random_note_length

# Tests ----------------------------------------------------------------


def test_random_note_length(common_rhythms, all_rhythms):
    """This test checks our random note length generation function.

    For every rhythm in our fixture of common lengths, run assertion:

    - Must be a valid Mingus rhythm. See 'mingus_rhythms' fixture.
    - Cannot be a data type other than an integer or float.
    """

    for key, rhythms in common_rhythms.items():
        rhythm = random_note_length(rhythms)
        assert rhythm in all_rhythms
        assert isinstance(rhythm, (int, float)) is True

