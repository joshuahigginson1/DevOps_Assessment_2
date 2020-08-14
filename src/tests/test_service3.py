# This file contains the functions for service2 Implementation 1 & 2.

# Imports --------------------------------------------------------------------------------

from src.service3.service3 import random_note_length


# Classes --------------------------------------------------------------------------------


# Functions ------------------------------------------------------------------------------


# Methods --------------------------------------------------------------------------------


# Define Variables -----------------------------------------------------------------------

# Execute Code ---------------------------------------------------------------------------

def test_random_note_length(common_rhythms, all_rhythms):
    for key, rhythms in common_rhythms.items():  # For every rhythm in our fixture of common lengths, run assertion.
        rhythm = random_note_length(rhythms)
        assert rhythm in all_rhythms  # Must be a valid Lilypond rhythm. See 'lilypond_rhythms' fixture.
        assert isinstance(rhythm, (int, str)) is True  # Cannot be a data type other than an integer or string.
