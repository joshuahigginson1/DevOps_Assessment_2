"""This file contains the functions for service1."""

# Imports --------------------------------------------------------------

import json
from os import environ
from dotenv import load_dotenv

from requests import Response

from src.service1_routes import service1, add_header, get_service_2_response, \
    get_service_3_response, random_download_text, get_png_download_name, \
    listify, get_midi_download_name, convert_form_to_full_json_output, \
    service_1_json_bundle

from unittest.mock import Mock, patch


# Test Logic -----------------------------------------------------------


def test_random_download_text(dl_text_list):
    """This function tests our random download test generator for our
    homepage.

    This function utilises the pytest fixture "dl_text_list".

    We expect that this function:
        - Returns a string.
        - Returns back a string from the dl_text_list.
    """

    random_text = random_download_text()

    assert isinstance(random_text, str)
    assert random_text in dl_text_list


def test_get_png_download_name():
    """This test checks the functionality of our png download name maker.

    We expect:
        - Any text going into our function comes back prefixed
          with '-melodie.png'

        - Returns a string.
    """

    for file_name in range(20):
        assert get_png_download_name(file_name).endswith("-melodie.png")

    assert isinstance(get_png_download_name("I'm a string"), str)
    assert isinstance(get_png_download_name(12345), str)


def test_get_midi_download_name():
    """This test checks the functionality of our midi download name maker.

    We expect:
        - Any text going into our function comes back prefixed
          with '-melodie.mid'

        - Returns a string.
    """

    for file_name in range(20):
        assert get_midi_download_name(file_name).endswith("-melodie.mid")

    assert isinstance(get_midi_download_name("I'm a string"), str)
    assert isinstance(get_midi_download_name(12345), str)


def test_listify():
    """When using WTForms, lists and tuples will be rendered as a string.
    This test checks our 'listify' function, which uses literal
    evaluation to fully ensure that our input list REALLY is a list.

    We expect:
    - Any string representation of a list will return a list object.
    """

    assert listify("[1, 2, 3, 4]") == [1, 2, 3, 4]
    assert isinstance(listify("[1, 2, 3, 4]"), list)


def test_convert_form_to_full_json_output(common_rhythms, common_scales):
    """This test checks the functionality of our WTForms output function.

    This function uses the fixtures:
    'common_rhythms' & 'common_scales'

     We expect:
     - To return a dictionary object.
     - The items within our dictionary will always be a key-value pair from
     it's parent.
     """

    # For rhythms.

    rhythm_form_selection = "[1, 2, 4]"

    r = convert_form_to_full_json_output(rhythm_form_selection, common_rhythms)

    assert isinstance(r, dict)

    assert list(r.keys())[0] in list(common_rhythms.keys())
    assert list(r.values())[0] in list(common_rhythms.values())

    # For scales.

    scale_form_selection = '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "r"]'

    s = convert_form_to_full_json_output(scale_form_selection, common_scales)

    assert list(s.keys())[0] in list(common_scales.keys())
    assert list(s.values())[0] in list(common_scales.values())

    assert isinstance(s, dict)


def test_post_service_1_json_bundle():
    """ This function tests the ability of python to bundle all of the given
    inputs into a dictionary."""

    test_bundle = service_1_json_bundle('A', (4 / 4), 120, "test", {"notes": [
        1]}, {"rhythms": [4]}, "A", 4)

    assert isinstance(test_bundle, dict)


def test_validate_on_submit_function():
    """

    """
    # TODO

    assert True


# Test API Responses ----------------------------------------------------


def test_post_service_2_response(mingus_pitches):
    """
    By entering a scale_key_pair, we expect to get back a random note pitch
    in said scale, as a musical note in string format.

    This test uses the pytest fixture 'Mingus_pitches'.

    """
    # TODO - I have no idea why or how to test this function.

    assert True


def test_post_service_3_response():
    """

    """
    # TODO - I have no idea why or how to test this function.

    assert True


# Test Routes ----------------------------------------------------------

def test_production_config():
    """This app checks the functionality of our .config file switcher."""

    service1.config.from_object('service1_config.TestingConfig')

    assert service1.config.get("TESTING") is True
    assert service1.config.get("DEBUG") is False

    service1.config.from_object('service1_config.ProductionConfig')

    assert service1.config.get("TESTING") is False
    assert service1.config.get("DEBUG") is False

    service1.config.from_object('service1_config.DevelopmentConfig')

    assert service1.config.get("TESTING") is False
    assert service1.config.get("DEBUG") is True


def test_add_header():
    """This function tests our wrapper function,
     which adds Cache Control to every response
      which was returned 'after request'

    """

    test_response = Response()

    # Before adding header...

    assert test_response.headers == {}

    # After adding header ...

    add_header(test_response)

    assert test_response.headers == {'Cache-Control': 'public, max-age=0',
                                     'Pragma': 'no-cache',
                                     'Expires': '0'}


# Test Return Form -----------------------------------------------------


def test_return_form(common_rhythms, common_scales):
    """


    This test utilises the pytest fixtures:
    'common_rhythms' & 'common_scales'.

    This test mocks:
        an s2 GET request as response -> common_scales..
        an s3 GET request as response -> common_rhythms.

    """

    client = service1.test_client()

    # We should always be able to reach the homepage, so a get request
    # should return 200.


def test_download_file():
    """This function tests the ability for our service to download a file."""

    client = service1.test_client()

    file_not_found = client.get('/there_are_no_files_with_this_name')
    png_file_found = client.get('/test-file-melodie.png')
    midi_file_found = client.get('/test-file-melodie.mid')

    assert file_not_found.status_code == 404
    assert png_file_found.status_code == 200
    assert midi_file_found.status_code == 200
