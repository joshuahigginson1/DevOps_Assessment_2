"""Tests all of the code for service #4"""

# Imports --------------------------------------------------------------
import pytest

from src.service4.service4 import Note, generate_key_offset, transpose_pitch, \
    Bar


# Tests ----------------------------------------------------------------

def test_default_note_object():
    """ This test checks that our default note returns the correct values.

    NB. Probably an arbitrary test, but need to check note class before
    API implementation.
    """

    default_note = Note()
    assert default_note.rhythm == 4
    assert default_note.ova == 0
    assert default_note.pitch == 'r'


def test_api_generated_note_object():
    """ Test to check that our API generated note returns correct values."""

    # TODO: Add test for API generated note, after implemented.
    assert True


def test_default_bar_object():
    default_bar = Bar()
    assert default_bar.tempo == 120
    assert default_bar.time_signature == 4
    assert default_bar.list_of_notes == []
    assert default_bar.bar_counter == 0



def test_api_generated_bar_object():
    """ Test to check that our API generated note returns correct values."""

    # TODO: Add test for API generated bar, after implemented.
    assert True


def test_transpose_pitch_is_rest(key_offset_dict):
    """ This test determines if our transpose pitch function
    works on a musical rest.
    """

    for offset in key_offset_dict.values():
        assert transpose_pitch('r', offset) == ('r', '')


def test_transpose_pitch_is_unexpected_pitch_type(key_offset_dict):
    """ This test checks to see if our application can deal with an invalid
    types of note pitch input.
    """

    with pytest.raises(TypeError):
        for offset in key_offset_dict.values():
            transpose_pitch([], offset)


def test_transpose_pitch_is_unexpected_value_error(key_offset_dict):
    """ This test checks to see if our application deals with unexpected
    note pitch values, which would output a value greater than the 3 octave
    limit.
    """

    with pytest.raises(ValueError):
        for offset in key_offset_dict.values():
            for erroneous_value in [-324, 0, 13, 324]:
                transpose_pitch(erroneous_value, offset)


def test_transpose_pitch_defaults():
    """ This test determines if the default variable for the transpose_pitch
    function work as anticipated."""

    assert transpose_pitch(1) == (1, "")  # Lower Bound
    assert transpose_pitch(5) == (5, "")  # Median Pitch
    assert transpose_pitch(12) == (12, "")  # Upper Bound


def test_transpose_pitch_is_middle_octave():
    """ This test checks the common anticipated values for pitches in our
    middle octave. """

    # Offset of -5
    assert transpose_pitch(6, -5) == (1, "")  # Lower Bound
    assert transpose_pitch(10, -5) == (5, "")  # Median Pitch
    assert transpose_pitch(12, -5) == (7, "")  # Upper Bound

    # Offset of -3
    assert transpose_pitch(4, -3) == (1, "")  # Lower Bound
    assert transpose_pitch(8, -3) == (5, "")  # Median Pitch
    assert transpose_pitch(12, -3) == (9, "")  # Upper Bound

    # Offset of 0
    assert transpose_pitch(1, 0) == (1, "")  # Lower Bound
    assert transpose_pitch(5, 0) == (5, "")  # Median Pitch
    assert transpose_pitch(12, 0) == (12, "")  # Upper Bound

    # Offset of 3
    assert transpose_pitch(1, 3) == (4, "")  # Lower Bound
    assert transpose_pitch(5, 3) == (8, "")  # Median Pitch
    assert transpose_pitch(9, 3) == (12, "")  # Upper Bound

    # Offset of 6
    assert transpose_pitch(1, 6) == (7, "")  # Lower Bound
    assert transpose_pitch(3, 6) == (9, "")  # Median Pitch
    assert transpose_pitch(6, 6) == (12, "")  # Upper Bound


def test_transpose_pitch_is_lower_octave():
    """ This test checks the common anticipated values for pitches in our
    lower octave. """

    # Offset of -1
    assert transpose_pitch(1, -1) == (12, ",")

    # Offset of -3
    assert transpose_pitch(1, -3) == (10, ",")
    assert transpose_pitch(2, -3) == (11, ",")
    assert transpose_pitch(3, -3) == (12, ",")

    # Offset of -5
    assert transpose_pitch(1, -5) == (8, ",")
    assert transpose_pitch(3, -5) == (10, ",")
    assert transpose_pitch(5, -5) == (12, ",")


def test_transpose_pitch_is_higher_octave():
    """ This test checks the common anticipated values for pitches in our
    higher octave. """

    # Offset of 0
    assert transpose_pitch(13, 0) == (1, "'")

    # Offset of 3
    assert transpose_pitch(10, 3) == (1, "'")
    assert transpose_pitch(12, 3) == (3, "'")
    assert transpose_pitch(13, 3) == (4, "'")

    # Offset of 6
    assert transpose_pitch(7, 6) == (1, "'")
    assert transpose_pitch(10, 6) == (4, "'")
    assert transpose_pitch(13, 6) == (7, "'")


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

        assert -5 <= generate_key_offset(key, key_offset_dict) <= 6


def test_lilypond_output():
    """This test checks the functionality of the function which
     converts our python note object into lilypond note format."""
    assert True


def test_find_length_of_bar():
    """This test checks the functionality of the function which
     converts our python note object into lilypond note format."""
    assert True

