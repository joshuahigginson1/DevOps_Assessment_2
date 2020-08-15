"""This file contains the functions for service4 Implementation 1 & 2."""


# Imports --------------------------------------------------------------


# Classes --------------------------------------------------------------

class Note:
    """ For our two api services to come together, we need to 'merge' the
    results into a representation of a single musical note.

    This is done here using a class object in Python.
    """

    def __init__(self, pitch="r", ova=0, rhythm=4):
        """ This code is ran upon initialisation of a note.

        Keyword Arguments:
            rhythm: The note length, in Lilypond format. Defaults to a quarter
            note.

            ova: The current octave, in Lilypond format. Defaults to the
            octave below middle C.

            pitch: The musical pitch, in Lilypond format. Defaults to a
            musical rest.
        """
        self.pitch = pitch
        self.ova = ova
        self.rhythm = rhythm


# Functions ------------------------------------------------------------

def generate_key_offset(user_input_key):
    """ A function which takes a given user's key, and offsets it to the key
    of f.

    Keyword Arguments:
        user_input_key: The key of our musical phrase, set by the user in
        service 1.

    Variables:



    """
    pass


def arbitrary_value_to_musical_scale(proprietary_gen_pitch, user_input_key):
    pitch_to_map = proprietary_gen_pitch
    pass


# Define Variables -----------------------------------------------------





# Execute Code ---------------------------------------------------------
