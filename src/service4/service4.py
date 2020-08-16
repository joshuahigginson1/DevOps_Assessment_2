"""This file contains the functions for service4 Implementation 1 & 2."""


# Imports --------------------------------------------------------------


# Classes --------------------------------------------------------------

class Note:
    """ For our two api services to come together, we need to 'merge' the
    results into a representation of a single musical note.

    This is done here using a class object in Python.
    """

    def __init__(self, transposed_pitch="r", ova=0, rhythm=4):
        """ This code is ran upon initialisation of a note.

        Keyword Arguments:
            self.rhythm: The note length, in Lilypond format. Defaults to 1/4
             note.

            self.ova: The current octave, in Lilypond format. Defaults to the
             octave below middle C.

            self.transposed_pitch: The musical pitch, in Lilypond format.
             Defaults to a musical rest.
        """
        self.pitch = transposed_pitch
        self.ova = ova
        self.rhythm = rhythm


class Bar:
    """In music theory, bars contain a number of notes that make up our
    melody.
    """

    def __init__(self, tempo=120, beats_in_bar=4):
        """This code is ran upon initialisation of our Bar.

        Keyword Arguments:
            self.tempo: The tempo of our piece in BPM. How fast or slow
             Defaults to 120bpm.

            self.time_signature: How many beats are in our bar.

            self.list_of_notes: The notes which comprise our bar. Should be
             comprised of note objects.
        """
        self.tempo = tempo
        self.time_signature = beats_in_bar
        self.list_of_notes = []
        self.bar_counter = 0



# Functions ------------------------------------------------------------

# This should really be in service #1, so all we send through API is one value.


def generate_key_offset(input_key, key_offset_dictionary):
    """ A function which takes a given user's key, and offsets it to the key
    of F chromatic.

    We add our key_offset to the current pitch value.
    We return a transposed index position (from the key of F chromatic).

    Keyword Arguments:
        input_key: The key of our musical phrase, set by the user in
        service #1.

        key_offset_dictionary: A mapping of each musical key in relation to
        key of F. This should be in the form of a python dictionary.
    """

    return key_offset_dictionary.get(input_key)


def transpose_pitch(raw_note_pitch, transposed_key_value=0):
    """ This function takes a raw note pitch and our transposed key value,
    and will transpose the output accordingly, adding a new octave flag if
    necessary.

    - Check to see if the raw note pitch is a musical note, or a rest.
    - Check if our value is out of bounds.
    - Transpose objects needing no octave flag.
    - Transpose objects needing a lower octave flag.
    - Transpose objects needing a higher object flag.
    - Return our transposed note pitch.

    Keyword Arguments:
        raw_note_pitch: This is the randomly generated note pitch from
         service #2.

        transposed_key_value: This is the transposed key value, AKA the
         output from the function in service #1 - 'generate_key_offset'. This
         defaults to 0 - the key of F chromatic.
    """
    transposed_ova = ""

    if raw_note_pitch == "r":
        transposed_pitch = "r"

    elif raw_note_pitch < 0 or raw_note_pitch > 13:
        raise ValueError("You should enter a value between 1 and 13.")

    # If raw note pitch is between 1 and 12, we don't add an octave flag.

    elif 1 <= (raw_note_pitch + transposed_key_value) <= 12:
        transposed_pitch = raw_note_pitch + transposed_key_value

    # If note pitch is transposed lower than our pitch range, add -1 ova flag.

    elif (raw_note_pitch + transposed_key_value) < 1:
        transposed_pitch = raw_note_pitch + transposed_key_value + 12
        transposed_ova = ","

    # If note pitch is transposed higher than our pitch range, add +1 ova flag.

    elif raw_note_pitch + transposed_key_value > 12:
        transposed_pitch = raw_note_pitch + transposed_key_value - 12
        transposed_ova = "'"

    else:
        raise TypeError("")

    return transposed_pitch, transposed_ova


def melodie_to_lilypond():
    """This function converts our note object into a lilypond object"""

    # TODO: Change proprietary to lilypond.
    pass


def midi_output():
    pass


def image_output():
    pass
