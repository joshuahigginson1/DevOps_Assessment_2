"""This file contains the functions for service2 Implementation 1 & 2."""

# Imports --------------------------------------------------------------

from service2 import return_scale_dictionary, \
    return_random_pitch, generate_random_note_pitch, get_note_name, \
    on_get_request, on_post_request


# Test Functions -------------------------------------------------------


def test_return_scale_dictionary(all_pitches):
    """This function tests our 'return scale dictionary' function.

        This test utilises our 'all_pitches' pytest fixture.

    - Return a dictionary.
    - Keys must be in lower case.
    - Scales can only be a number between 1 to 12, or "r".
    """

    check_dictionary = return_scale_dictionary()
    assert isinstance(check_dictionary, dict)

    for scale_name, scale_list in list(return_scale_dictionary().items()):

        assert scale_name.islower()

        for note in scale_list:
            assert note in all_pitches


def test_generate_random_note_pitch(common_scales, all_pitches):
    """This test checks our random note pitch function.

    This test utilises the pytest fixtures: common_scales & all_pitches.

    Every scale in our fixture of common scales:
    - Cannot be out of an octave bounds.
    - Cannot be a data type other than an integer or string.
    """

    for key, scales in common_scales.items():
        note = generate_random_note_pitch(scales)
        assert note in all_pitches
        assert isinstance(note, (int, str)) is True


def test_get_note_name(note_names_in_c):
    """This test checks our 'get note name' function.

    This test utilises our 'note_names_in_c' pytest fixture.

    - We cannot generate a note pitch which is not deemed a 'real'
    musical note by Mingus or Lilypond.

    """
    for note_pitch in note_names_in_c:
        note_name = note_names_in_c.get(note_pitch)
        assert get_note_name(note_pitch, note_names_in_c) == note_name


def test_return_random_pitch(note_names_in_c, common_scales):
    """This test checks our 'return random pitch' function.

        This test utilises the pytest fixtures:
        'note_names_in_c' & 'common_scales'.

    - The output note name must be in our note_names_in_c dictionary.
    - It must be a string output.
    """
    for key, scale in common_scales.items():
        random_note_name = return_random_pitch(scale)

        assert random_note_name in note_names_in_c.values()

        assert isinstance(random_note_name, str)


# Test API Requests ----------------------------------------------------


def test_on_get_request(common_scales):
    """This function tests our GET request functionality for our API.

        This test utilises the pytest fixture 'common_scales'.

    When we send a get req to service 2, we should:
    - GET a status code 200.
    - GET a JSON file, containing a list of our common scales.








    """
    # TODO: Write unit test for on_get_request().
    assert True


def test_on_post_request():
    """This function tests our POST request functionality for our API."""
    # TODO: Write unit test for on_post_request().

    assert True
