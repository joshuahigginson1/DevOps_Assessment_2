"""This file contains the functions for service2 Implementation 1 & 2.

On a GET request, we want our program to provide a list of musical scales,
for our user to pick from.

On a POST request, we want out program to return a random note.
"""

# Imports --------------------------------------------------------------

import random

from os import environ

from flask import Flask, jsonify, request

# Flask ----------------------------------------------------------------

# Create our flask application.

service2 = Flask(__name__)

if environ.get("FLASK_ENV").replace('"', '') == 'production':

    service2.config.from_object('service2_config.ProductionConfig')

elif environ.get("FLASK_ENV").replace('"', '') == 'testing':
    service2.config.from_object('service2_config.TestingConfig')

else:
    service2.config.from_object('service2_config.DevelopmentConfig')


# On GET Request -------------------------------------------------------
# Helper Functions -----------------------------------------------------


def return_scale_dictionary():
    """This function is to be used with a GET request, returning a list of
    scales for our user to select from.

    Service #1 requires a list of pitches for our user to chose from. The
    different implementations of service #2 will alter these pitch lists.

    When Service #2 receives a GET request, it will send the output.
    """

    scale_list = {
        "chromatic": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "r"],
        "major": [1, 3, 5, 6, 8, 10, 12, "r"],
        "major pentatonic": [1, 3, 5, 8, 10, "r"],
        "major blues": [1, 3, 4, 5, 8, 10, "r"],
        "natural minor": [1, 3, 4, 6, 8, 9, 11, "r"],
        "harmonic minor": [1, 3, 4, 6, 8, 9, 12, "r"],
        "minor pentatonic": [1, 4, 6, 8, 11, "r"],
        "minor blues": [1, 4, 6, 7, 8, 11, "r"],
        "png implementation": [1, 4, 6, 7, 8, 11, "r"]
    }

    return scale_list


# Function -------------------------------------------------------------


@service2.route('/', methods=['GET'])
def on_get_request():
    """This function triggers after every get request, to the endpoint '/'"""

    # TODO: Write unit test for on_get_request().

    return jsonify(return_scale_dictionary())


# On POST Request ------------------------------------------------------
# Helper Functions -----------------------------------------------------

def generate_random_note_pitch(scale_list):
    """Generate a random note pitch determinant on the scale list.

    Keyword Arguments:
        scale_list: A list of Mingus compatible pitches, in a list.
    """
    return random.choice(scale_list)


def get_note_name(generated_note_pitch, note_names_in_c):
    """Converts our randomised note pitch into musical notes in the key of C.

    Keyword Arguments:
        generated_note_pitch: Our randomly generated note pitch.

        note_names_in_c: A dictionary of the note positions in the C
         chromatic scale, and their corresponding note names.
    """
    return note_names_in_c.get(generated_note_pitch)


def return_random_pitch(user_chosen_scale):
    """This function is to be used with a POST request, returning a random
    note pitch, based on the user's chosen scale.

    Keyword Arguments:
        user_chosen_scale: A musical scale, chosen by the user as a result
        of a GET request to the service #2 API.
    """
    c_chromatic_dictionary = {  # Notes an corresponding positions of C chrom.
        1: 'C',
        2: 'C#',
        3: 'D',
        4: 'D#',
        5: 'E',
        6: 'F',
        7: 'F#',
        8: 'G',
        9: 'G#',
        10: 'A',
        11: 'A#',
        12: 'B',
        "r": "r"
    }

    rand_note_pitch = generate_random_note_pitch(user_chosen_scale)
    return get_note_name(rand_note_pitch, c_chromatic_dictionary)


# Function -------------------------------------------------------------


@service2.route('/', methods=['POST'])
def on_post_request():
    """This function triggers after every post request to the endpoint '/'
    We expect to receive a specific set of notes from service 1.
    """

    # TODO: Write unit test for on_post_request().

    received_data = request.get_json()
    print(f"Received data = {received_data}")

    converted_data = list(received_data.values())
    print(f"Converted data = {converted_data}")

    note_pitch_output = return_random_pitch(converted_data[0])
    print(f'Converted data: {converted_data[0]}')
    print(f'Note pitch output: {note_pitch_output}')
    return jsonify(note_pitch_output)
