"""This file contains the functions for service4 Implementation 1 & 2."""

# Imports --------------------------------------------------------------

from mingus.containers import Bar
from mingus.midi import midi_file_out
from mingus.extra.lilypond import to_png, from_Bar


# Functions ------------------------------------------------------------


def generate_key_offset(input_key, key_offset_dictionary):
    """ A function which takes a given user's key, and offsets it to the key
    of C chromatic.

    We add our key_offset to the current pitch value.
    We return a transposed index position (from the key of C chromatic).

    Keyword Arguments:
        input_key: The key of our musical phrase, set by the user in
         service #1.

        key_offset_dictionary: A mapping of each musical key in relation to
         key of C. This should be in the form of a python dictionary.
    """

    return key_offset_dictionary.get(input_key)

# Execute Code ---------------------------------------------------------


output_key = "C"  # From Service #1
output_time_signature = 4, 4  # From Service #1

# Create new bar.

output_bar = Bar(output_key, output_time_signature)

# Pull a note pitch from service #2.

first_note_pitch = "C"

# Pull a note length from service #3.

first_note_length = 6

# While our output bar is not full, we will keep trying to add notes to it.
# Return False if there is room in this Bar for another Note True otherwise.

while not output_bar.is_full():
    # We try and add the note to our bar.

    # If note is rest, we call function place_rest().

    if first_note_pitch == "r":
        output_bar.place_rest(first_note_length)

    # If note is note, we call function place_notes().

    else:
        output_bar.place_notes(first_note_pitch, first_note_length)

    # Poll API for another note.
    # Rinse and repeat until bar is full.


# Transpose output bar to a given user key.

key_to_transpose = 5  # From generate key offset function.
transpose_up_or_down = True  # True is up, False is down. From Service #1

output_bar.transpose(str(key_to_transpose), transpose_up_or_down)

# Save as MIDI

output_beats_per_minute = 120  # From service #1

file_name = "josh-test-midi-file"  # From service #1
midi_file_suffix = file_name + "-melodie.mid"
midi_save_location = "midi_output/" + midi_file_suffix

midi_file_out.write_Bar(midi_save_location, output_bar,
                        output_beats_per_minute)


lilypond_string = from_Bar(output_bar, showkey=True, showtime=True)

# This feature will only work with lilypond in path. Save as lilypond string.

png_save_location = f"png_output/{file_name}-melodie"

to_png(lilypond_string, png_save_location)  # Exports lilypond
# string to png.

# Deprecated Functions -------------------------------------------------


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
