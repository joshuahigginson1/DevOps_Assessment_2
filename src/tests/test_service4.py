"""Tests all of the code for service #4"""

# Imports --------------------------------------------------------------

from src.service4.service4 import Note


# Tests ----------------------------------------------------------------

def test_default_note_object():
    """ This test checks that our default note returns the correct values.

    NB. Probably an arbitrary test, but need to check note class before
    API implementation.
    """

    test_note = Note()
    assert test_note.rhythm == 4
    assert test_note.ova == 0
    assert test_note.pitch == 'r'


def test_api_generated_note_object():
    """ Test to check that our API generated note returns correct values."""

    # TODO: Add test for API generated note, after implemented.
    assert True


def test_arbitrary_value_to_musical_scale():
    """ This test checks the output of our our musical scale function,
    in order to ensure that the conversion returns expected values of a
    given musical scale.
    """
    assert True


def test_generate_key_offset():
    """ This test checks the functionality of our key offset function.
    """
    assert True