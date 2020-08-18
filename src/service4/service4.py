"""This file contains the functions for service4 Implementation 1 & 2."""

# Imports --------------------------------------------------------------
import json

from flask import jsonify
from mingus.containers import Bar
from mingus.midi import midi_file_out
from mingus.extra.lilypond import to_png, from_Bar

import requests


# Functions ------------------------------------------------------------

def unpack_json():
    """This function will unpack our JSON data into expected variables."""

    s1_key = "C"  # From Service #1
    s1_time_signature = 4, 4  # From Service #1
    s1_tempo = 120  # From service #1
    s1_file_name = "josh-test-midi-file"  # From service #1
    s1_user_scale_key_pair = {"major blues": [1, 3, 4, 5, 8, 10, "r"]}
    s1_user_rhythm_key_pair = {"standard": [1, 2, 4, 8, 16, 32]}
    first_note_pitch = "C"  # Pull a note pitch from service #2.
    first_note_length = 6  # Pull a note length from service #3.


def create_bar(user_key, user_time_signature):
    """This function returns a new Mingus bar object.
    Keyword Arguments:
        user_key: TODO
        user_time_signature: TODO
        """
    return Bar(user_key, user_time_signature)


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


# Our post request will send all of this data over in a neat json format.


def post_service2(url, scale_key_pair):
    """Using our existing user data from s1, we use this function to
    send a post request to s2, for a new note pitch.

    Keyword Arguments:
        url: The url of service 2.
        scale_key_pair: A key pair scale list dictionary.

    """

    service_2_response = requests.post(url, json=scale_key_pair)
    json_response_data = service_2_response.json()
    status_code_response = service_2_response.status_code

    print("\n ----------- Service 2 POST Response ----------- \n")

    print(f'Data: {json_response_data}')
    print(f'Response Code: {status_code_response}')

    print("\n ----------- End of Service 2 POST Response ----------- \n")

    return json_response_data


def post_service3(url, rhythm_key_pair):
    """Using our existing user data from s1, we use this function to
    poll s3 with a post request for a new note length.

    Keyword Arguments:
        url: The url of service 3.
        rhythm_key_pair: A key pair rhythm list dictionary.

    """

    service_3_response = requests.post(url, json=rhythm_key_pair)
    json_response_data = service_3_response.json()
    status_code_response = service_3_response.status_code

    print("\n ----------- Service 3 POST Response ----------- \n")

    print(f'Data: {json_response_data}')
    print(f'Response Code: {status_code_response}')

    print("\n ----------- End of Service 3 POST Response ----------- \n")

    return json_response_data


def initialise_bar(bar_object, note_length, note_pitch):
    """This function adds a new note to an existing bar object.
    Keyword Arguments:
        bar_object: Our empty mingus bar object.
        note_length: A given note length in mingus syntax.
        note_pitch: A given note pitch in mingus syntax.
        """
    # TODO: Test add_note_to_bar function

    if note_pitch == "r":
        return bar_object.place_rest(note_length)

    # If note is note, we call function place_notes().
    else:
        return bar_object.place_notes(note_pitch, note_length)


def add_notes_to_bar(initialised_bar):
    """This function fills an existing bar object with new notes, polled
    from service 2 and service 3.
    """
    # TODO: Test fill_bar_with_notes function
    bar_object = initialised_bar

    # While the bar is not full, we try and add a new note to the bar.
    while not bar_object.is_full():
        # We poll service 2 and 3 for a new note, and add to bar.
        filled = initialised_bar(bar_object, poll_service3(), poll_service2())

    # When the bar is full, it will break out of this loop, and return a
    # full bar.

    return filled


def transpose_bar(full_bar, key_to_transpose, transpose_up_or_down=True):
    """This function transposes our full bar, dependent on the user's
    chosen key signature in service 1."""

    key_to_transpose = 5  # From generate key offset function.

    full_bar.transpose(str(key_to_transpose), transpose_up_or_down)


def save_as_midi(file_name, output_bar, user_tempo):
    """TODO"""
    midi_file_suffix = file_name + "-melodie.mid"
    midi_save_location = "midi_output/" + midi_file_suffix

    return midi_file_out.write_Bar(midi_save_location, output_bar,
                                   user_tempo)


def save_as_png(file_name, output_bar):
    """This file generates a lilypond string from our mingus bar, and saves
    it as a PNG file.
        Keyword Arguments:
            file_name: The user's chosen file name.png
            output_bar: A full mingus bar.
    """
    lilypond_string = from_Bar(output_bar, showkey=True, showtime=True)

    # This feature will only work with lilypond in path.

    png_save_location = f"png_output/{file_name}-melodie"

    return to_png(lilypond_string, png_save_location)


service_2_url = "http://0.0.0.0:5002/"
service_3_url = "http://0.0.0.0:5003/"

s1_user_scale_key_pair = {"major blues": [1, 3, 4, 5, 8, 10, "r"]}
s1_user_rhythm_key_pair = {"standard": [1, 2, 4, 8, 16, 32]}

post_service2(service_2_url, s1_user_scale_key_pair)
post_service3(service_3_url, s1_user_rhythm_key_pair)
