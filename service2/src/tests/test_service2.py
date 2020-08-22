"""This file contains the functions for service2 Implementation 1 & 2."""

# Imports --------------------------------------------------------------

import json
from os import environ

from src.service2 import return_scale_dictionary, \
    return_random_pitch, generate_random_note_pitch, get_note_name, \
    on_get_request, on_post_request, service2


# Test Flask App Config ------------------------------------------------

def test_production_config():
    """This app checks the functionality of our .config file switcher."""

    assert service2.config['ENV'] == environ.get('ENV')

    service2.config.from_object('service2_config.TestingConfig')

    assert service2.config.get("TESTING") is True
    assert service2.config.get("DEBUG") is False

    service2.config.from_object('service2_config.ProductionConfig')

    assert service2.config.get("TESTING") is False
    assert service2.config.get("DEBUG") is False

    service2.config.from_object('service2_config.DevelopmentConfig')

    assert service2.config.get("TESTING") is False
    assert service2.config.get("DEBUG") is True

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

    client = service2.test_client()

    response = client.get('/')

    # Converts our JSON response to a python dictionary.
    decode_response = json.loads(response.get_data())

    assert response.status_code == 200
    assert decode_response == common_scales


def test_on_post_request(all_pitches, note_names_in_c):
    """
    This function tests our POST request functionality for our API.

    This test will utilise the pytest fixtures 'note_names_in_c'.

    When we receive a post request to service 2, we expect:

    - To receive data in a scale key-pair format.

    - To return a status code of 200.

    - To return to get back a single note, as string.

    """

    client = service2.test_client()

    scale_key_pair = {'chromatic': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                    'r']}

    response = client.post('/', json=scale_key_pair)
    response_data = response.get_data().decode("utf-8")
    response_data = response_data.rstrip("\n").strip('"')

    assert response_data in note_names_in_c.values()
    assert response.status_code == 200
