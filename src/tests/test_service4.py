"""Tests all of the code for service #4"""

# Imports --------------------------------------------------------------

from src.service4.service4 import generate_key_offset

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

    for key in all_keys:
        # assert generate_key_offset(key, key_offset_dict) == \
        #       key_offset_dict.get(key)  # Is this test needed?

        assert 0 <= generate_key_offset(key, key_offset_dict) <= 11
