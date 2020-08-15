# This file contains the functions for service2 Implementation 1 & 2.

# Imports --------------------------------------------------------------

from src.service2.service2 import random_note_pitch

# Classes --------------------------------------------------------------


# Functions ------------------------------------------------------------


# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------

# Execute Code ---------------------------------------------------------

def test_random_note_pitch(common_scales, all_pitches):
    """This test checks our random note pitch function.

    For every scale in our fixture of common scales, run our assertion:

    - Cannot be out of an octave bounds.
    - Cannot be a data type other than an integer or string.
    """

    for key, scales in common_scales.items():
        note = random_note_pitch(scales)
        assert note in all_pitches
        assert isinstance(note, (int, str)) is True
