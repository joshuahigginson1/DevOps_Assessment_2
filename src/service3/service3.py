"""This file contains the functions for service3 Implementation 1 & 2.

On a GET request, we want our program to provide a list of note lengths,
for our user to pick from.

On a POST request, we want out program to return a random note length..
"""

# Imports --------------------------------------------------------------

import random


# On GET Request -------------------------------------------------------
# Functions ------------------------------------------------------------

def return_length_dictionary():
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


# On POST Request ------------------------------------------------------
# Functions ------------------------------------------------------------

def random_note_length(common_rhythms):
    """This function is to be used with a POST request, generating a random
    note length from a given list.

    Keyword Arguments:
        common_rhythms: A list of common note rhythms, in Mingus format.
    """
    return random.choice(common_rhythms)
