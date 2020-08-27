"""This file contains the tests for service3 Implementation 1 & 2."""

# Imports --------------------------------------------------------------
import json

from src.service3 import random_note_length, service3, \
    return_rhythms_dictionary

# Test Flask App Config ------------------------------------------------


def test_production_config():
    """This app checks the functionality of our .config file switcher."""

    client = service3.test_client()

    service3.config.from_object('service3_config.TestingConfig')

    assert service3.config.get("TESTING") is True
    assert service3.config.get("DEBUG") is False

    service3.config.from_object('service3_config.ProductionConfig')

    assert service3.config.get("TESTING") is False
    assert service3.config.get("DEBUG") is False

    service3.config.from_object('service3_config.DevelopmentConfig')

    assert service3.config.get("TESTING") is False
    assert service3.config.get("DEBUG") is True


# Test Functions -------------------------------------------------------


def test_return_rhythms_dictionary(all_rhythms):
    """This test checks the main function behind s3.

    This test utilises our 'all_rhythms' pytest fixture.

    - Return a dictionary.
    - Keys must be in lower case.
    - Rhythms can only be returned in Mingus format.
    """

    check_dictionary = return_rhythms_dictionary()
    assert isinstance(check_dictionary, dict)

    for rhythm_name, rhythm_list in list(return_rhythms_dictionary().items()):

        assert rhythm_name.islower()

        for rhythm in rhythm_list:
            assert rhythm in all_rhythms


def test_random_note_length(common_rhythms, all_rhythms):
    """This test checks our random note length generation function.

    This test utilises the fixtures: 'all_rhythms' and 'common_rhythms'.

    For every rhythm in our fixture of common lengths, run assertion:

    - Must be a valid Mingus rhythm. See 'mingus_rhythms' fixture.
    - Cannot be a data type other than an integer or float.
    """

    for key, rhythms in common_rhythms.items():
        rhythm = random_note_length(rhythms)
        assert rhythm in all_rhythms
        assert isinstance(rhythm, (int, float)) is True


# Test API Requests ----------------------------------------------------


def test_on_get_request(common_rhythms):
    """This test checks our GET request functionality for our API.
        This test utilises the pytest fixture 'common_scales'.

    When we send a get req to service 2, we should:
    - GET a status code 200.
    - GET a JSON file, containing a list of our common rhythms.

    """

    client = service3.test_client()

    response = client.get('/')

    # Converts our JSON response to a python dictionary.
    decode_response = json.loads(response.get_data())

    assert response.status_code == 200
    assert decode_response == common_rhythms


def test_on_post_request(all_rhythms):
    """
    This function tests our POST request functionality for our API.

    This test will utilise the pytest fixture 'all_rhythms'.

    When we receive a post request to service 3, we expect:

    - To receive data in a rhythm key-pair format.

    - To return a status code of 200.

    - To return to get back a single rhythm, as int.

    """

    client = service3.test_client()

    rhythm_key_pair = {"all_rhythms": [1, 2, 4, 8, 16, 32, 64]}

    response = client.post('/', json=rhythm_key_pair)
    response_data = int(response.get_data())

    assert response_data in all_rhythms
    assert response.status_code == 200

