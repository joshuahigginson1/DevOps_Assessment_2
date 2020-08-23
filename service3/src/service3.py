"""This file contains the functions for service3 Implementation 1 & 2.

On a GET request, we want our program to provide a list of note lengths,
for our user to pick from.

On a POST request, we want out program to return a random note length..
"""

# Imports --------------------------------------------------------------

import random

from os import environ

from flask import Flask, request, jsonify

# Flask ----------------------------------------------------------------

# Create our flask application.

service3 = Flask(__name__)

if environ.get("FLASK_ENV") == 'production':
    service3.config.from_object('service3_config.ProductionConfig')

elif environ.get("FLASK_ENV") == 'testing':
    service3.config.from_object('service3_config.TestingConfig')

else:
    service3.config.from_object('service3_config.DevelopmentConfig')


# On GET Request -------------------------------------------------------
# Helper Functions -----------------------------------------------------

def return_rhythms_dictionary():
    """This function is to be used with a GET request, returning a list of
    note lengths for our user to select from.

    Service #1 requires a list of note lengths for our user to chose from. The
    different implementations of service #3 will alter these pitch lists.

    When Service #3 receives a GET request, it will send the output of this
    function.
    """

    # TODO: Write unit test for return_rhythms_dict() with API functionality.

    rhythms_dictionary = {
        "short": [4, 8, 16, 32],
        "long": [1, 2, 4],
        "standard": [2, 4, 8, 16],
        "extremes": [1, 32, 64, 128]
    }

    return rhythms_dictionary


# Function -------------------------------------------------------------


@service3.route('/', methods=['GET'])
def on_get_request():
    """This function triggers after every get request to the endpoint '/'"""

    return jsonify(return_rhythms_dictionary())


# On POST Request ------------------------------------------------------
# Helper Functions -----------------------------------------------------

def random_note_length(common_rhythms):
    """This function is to be used with a POST request, generating a random
    note length from a given list.

    Keyword Arguments:
        common_rhythms: A list of common note rhythms, in Mingus format.
    """
    return random.choice(common_rhythms)


# Function -------------------------------------------------------------


@service3.route('/', methods=['POST'])
def on_post_request():
    """This function triggers after every post request to the endpoint '/'
    We expect to receive a specific set of rhythms from service 1, in JSON
    format.

    We parse the JSON with function 'request.get_json(). This turns it into
    a python dictionary.

    We convert this dictionary into a list. Annoyingly because our data is
    already encapsulated as a list, this method creates  a 'list inside a list'
    This is why we must use index[0] to retrieve our data.

    We then run this data through our random function, to return a note length.

    """
    received_data = request.get_json()

    converted_data = list(received_data.values())
    note_length_output = random_note_length(converted_data[0])
    return jsonify(note_length_output)
