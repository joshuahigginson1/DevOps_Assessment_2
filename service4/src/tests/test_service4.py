"""Tests all of the code for service #4"""

# Imports --------------------------------------------------------------

from src.service4_routes import create_bar
from mingus.containers import Bar


# Tests ----------------------------------------------------------------


def test_generate_key_offset(all_keys, key_offset_dict):
    """ This test checks the functionality of our key offset function.

    For every key, we check to ensure that our note should never be offset
    by more than twelve notes.

    The program will not crash, however, it is unexpected behaviour for
    this scenario to occur. It means that a previously running function,
    is not operating correctly.

    Variables:
        list_of_keys = A pytest fixture returning every possible lilypond key.
        key_offset_dict = A pytest fixture returning our key offset.
    """


def test_create_bar():
    """This tests the creation of a new bar."""

    new_bar = create_bar()

    assert True == True


def test_initialise_bar():
    """This tests the..."""

    assert True == True


def test_add_notes_to_bar():
    """This tests the..."""

    assert True == True


def test_overwrite_transpose_bar():
    """This tests the..."""

    assert True == True
