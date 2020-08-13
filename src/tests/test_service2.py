# This file contains the functions for service2 Implementation 1 & 2.

# Imports --------------------------------------------------------------------------------

from src.service2.service2 import random_note_pitch

# Classes --------------------------------------------------------------------------------


# Functions ------------------------------------------------------------------------------


# Methods --------------------------------------------------------------------------------

chromatic_scales = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# Define Variables -----------------------------------------------------------------------


# Execute Code ---------------------------------------------------------------------------
def test_random_note_pitch():
    note = random_note_pitch(chromatic_scales)
    assert note >= 0
    assert isinstance(note, int) is True
