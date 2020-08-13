# This file contains the functions for service2 Implementation 1 & 2.

# Imports --------------------------------------------------------------------------------

from src.service2.service2 import random_note_pitch


# Classes --------------------------------------------------------------------------------


# Functions ------------------------------------------------------------------------------


# Methods --------------------------------------------------------------------------------


# Define Variables -----------------------------------------------------------------------

# Execute Code ---------------------------------------------------------------------------

def test_random_note_pitch(common_scales):
    for key, scales in common_scales.items():  # For every scale in our fixture of common scales, run our assertion.
        note = random_note_pitch(scales)
        assert 0 <= note <= 13  # Cannot be out of an octave bounds.
        assert isinstance(note, int) is True  # Cannot be a data type other than an integer.
