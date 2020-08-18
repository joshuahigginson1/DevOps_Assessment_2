"""This file contains the functions for service3 Implementation 1 & 2.

On a GET request, we want our program to provide a list of note lengths,
for our user to pick from.

On a POST request, we want out program to return a random note length..
"""

# Imports --------------------------------------------------------------

import random
from flask import Flask, Response, request, jsonify

# Flask ----------------------------------------------------------------

# Create our flask application.
service3 = Flask(__name__)


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

    # TODO: Write unit test for return_scale_dict() with API functionality.

    rhythms_dictionary = {
        "short": [8, 16, 32, 64],
        "long": [1, 2, 4],
        "standard": [1, 2, 4, 8, 16, 32],
        "extremes": [0.25, 0.5, 64, 128]
    }

    return rhythms_dictionary


# Function -------------------------------------------------------------


@service3.route('/', methods=['GET'])
def on_get_request():
    """This function triggers after every get request to the endpoint '/'"""
    return jsonify(return_rhythms_dictionary())


# On POST Request ------------------------------------------------------
# Helper Function ------------------------------------------------------

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
    We expect to receive a specific set of rhythms from service 1.
    """

    received_data = request.data.decode('utf-8')
    note_length_output = random_note_length(received_data)

    return Response(note_length_output, mimetype="text/plain")


# Run our service ------------------------------------------------------

if __name__ == "__main__":
    service3.run()
