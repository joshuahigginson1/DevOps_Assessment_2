"""This file contains the functions for service2 Implementation 1 & 2."""

# Imports --------------------------------------------------------------

import random

# Classes --------------------------------------------------------------


# Functions ------------------------------------------------------------

def random_note_pitch(pitch_list):
    """Generate a random note pitch determinant on the pitch list.

    Keyword Arguments:
        pitch_list: A list of Lilypond compatible pitches, in a list.
    """
    return random.choice(pitch_list)


def get_note_name(generated_note_pitch, note_names_in_c):
    """Converts our randomised note pitch into musical notes in the key of C.

    Keyword Arguments:
        generated_note_pitch: Our randomly generated note pitch.

        note_names_in_c: A dictionary of the note positions in the C
         chromatic scale, and their corresponding note names.
    """
    return note_names_in_c.get(generated_note_pitch)

# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------

# Execute Code ---------------------------------------------------------
