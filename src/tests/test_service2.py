"""This file contains the functions for service2 Implementation 1 & 2."""

# Imports --------------------------------------------------------------

from src.service2.service2 import random_note_pitch, get_note_name


# Classes --------------------------------------------------------------


# Functions ------------------------------------------------------------

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


def test_get_note_name(note_names_in_c):
    """This test checks our 'get note name' function.

    This test relies on the 'note_names_in_c pytest fixture.
    """
    for note_pitch in note_names_in_c:
        note_name = note_names_in_c.get(note_pitch)
        assert get_note_name(note_pitch, note_names_in_c) == note_name

# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------

# Execute Code ---------------------------------------------------------
