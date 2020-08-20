"""This file contains the tests for service3 Implementation 1 & 2."""

# Imports --------------------------------------------------------------

from service3.service3 import random_note_length

# Test Functions -------------------------------------------------------


def test_random_note_length(common_rhythms, all_rhythms):
    """This test checks our random note length generation function.

    For every rhythm in our fixture of common lengths, run assertion:

    - Must be a valid Mingus rhythm. See 'mingus_rhythms' fixture.
    - Cannot be a data type other than an integer or float.
    """

    for key, rhythms in common_rhythms.items():
        rhythm = random_note_length(rhythms)
        assert rhythm in all_rhythms
        assert isinstance(rhythm, (int, float)) is True


def test_return_rhythms_dictionary():
    """This test checks our GET request API functionality."""

    # TODO: Write unit test for return_rhythms_dict().
    assert True


# Test API Requests ----------------------------------------------------


def test_on_get_request():
    """This test checks our GET request functionality for our API."""
    # TODO: Write unit test for GET req API functionality.
    assert True


def test_on_post_request():
    """This test checks our POST request functionality for our API."""
    # TODO: Write unit test for POST req API functionality.
    assert True
