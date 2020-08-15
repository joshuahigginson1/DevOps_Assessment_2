# Task:

# Imports --------------------------------------------------------------


# Classes --------------------------------------------------------------

class Note:
    def __init__(self, pitch="r", ova=0, rhythm=4):
        """
        For our two apis will come together, we need to 'merge' the results
        in a representation of a musical note. This can be done using a
        class object in Python.

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


# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------


# Execute Code ---------------------------------------------------------
