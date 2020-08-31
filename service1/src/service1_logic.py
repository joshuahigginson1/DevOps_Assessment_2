"""This script contains all of our service 1 logic."""

# Imports --------------------------------------------------------------

import ast

import random

import requests

from src.service1_init import service1


# Functions ------------------------------------------------------------

def random_download_text():
    """When I was testing out the download button functionality, I found it
    difficult to know if a second or third file had been generated. This
    function alters the 'your file is ready' button randomly, to aid with
    user feedback."""

    dl_text_list = ["Your file is ready!",
                    "Your new file is ready to download!",
                    "Let's make some music - Download Now.",
                    "Let the music play! Your download link.",
                    "Download now!",
                    "Download here!"]

    return random.choice(dl_text_list)


def get_png_download_name(user_file_name):
    """This function takes the user's input file name,
     and returns the corresponding output png file name.

    Keyword Arguments:
        user_file_name: The file name entered by the user.
    """
    return f"{user_file_name}-melodie.png"


def get_midi_download_name(user_file_name):
    """This function takes the user's input file name,
    and returns the corresponding output midi file name.

    Keyword Arguments:
        user_file_name: The file name entered by the user.
    """
    return f"{user_file_name}-melodie.mid"


def listify(input_string):
    """WTForms annoyingly converts lists and tuples to string type.
    This function uses literal evaluation to redefine a list from a given
    string input.

    Keyword Arguments:
        input_string: A literal string which is masquerading as a list.
    """
    input_string = ast.literal_eval(input_string)
    return input_string


def convert_form_to_full_json_output(form_get_on_validation, full_dict):
    """WTForms cannot return dictionary key value pairs. This function
    takes the output of our WTForms and converts it to a dictionary format,
    relative to the original dictionary.

    Keyword Arguments:
        full_dict: The full dictionary in which we will be 'looking up'
        our key-value pairs.

        form_get_on_validation: The output of a form object after validation.
    """

    # Create a list of all key-value pairs from our full dictionary.
    list_of_dict_items = list(full_dict.items())
    output_form_list = listify(form_get_on_validation)

    # Initialise a new_dictionary.
    new_dict = {}

    # If a value in this dictionary matches the returned value...
    # ...from our form, then we return a new dictionary object.

    for label, value in list_of_dict_items:
        if value == output_form_list:
            new_dict = {label: value}

            print(f"new_dict: {new_dict}")

    return new_dict


def get_service_2_response(url):
    """This function posts a get response to service 2, and returns the
    output.

    Keyword Arguments:
        url: The url of service 2.
    """

    service_2_response = requests.get(url)
    decoded_service_2_response = service_2_response.json()

    print("\n ----------- Service 2 GET Response ----------- \n")
    print(decoded_service_2_response)
    print("\n ----------- End of Service 2 GET Response ----------- \n")
    return decoded_service_2_response


def get_service_3_response(url):
    """This function posts a get request to service 3, and returns the
    output.

    Keyword Arguments:
        url: The url of service 3.
    """

    service_3_response = requests.get(url)
    decoded_service_3_response = service_3_response.json()

    print("\n ----------- Service 3 GET Response ----------- \n")
    print(decoded_service_3_response)
    print("\n ----------- End of Service 3 GET Response ----------- \n")

    return decoded_service_3_response


def post_service_2_response(url, scale_key_pair):
    """Using the user entry for scale key-pair, we use this function to
    send a post request to s2, for a new note pitch.

    Keyword Arguments:
        url: The url of service 2.
        scale_key_pair: A key pair scale list dictionary.

    """

    service_2_response = requests.post(url, json=scale_key_pair)
    json_response_data = service_2_response.json()

    print("\n ----------- Service 2 POST Response ----------- \n")

    print(f'Service 2 Response: {service_2_response}')
    print(f'Response Code: {service_2_response.status_code}')
    print(f'Data: {json_response_data}')

    print("\n ----------- End of Service 2 POST Response ----------- \n")

    return json_response_data


def post_service_3_response(url, length_key_pair):
    """Using the user entry for length key-pair, we use this function to
    send a post request to s3, for a new note length.

    Keyword Arguments:
        url: The url of service 2.
        length_key_pair: A key pair scale list dictionary.

    """

    service_3_response = requests.post(url, json=length_key_pair)
    json_response_data = service_3_response.json()
    status_code_response = service_3_response.status_code

    print("\n ----------- Service 3 POST Response ----------- \n")

    print(f'Data: {json_response_data}')
    print(f'Response Code: {status_code_response}')

    print("\n ----------- End of Service 3 POST Response ----------- \n")

    return json_response_data


def service_1_json_bundle(key, time_signature, tempo, file_name,
                          scale_key_pair, rhythm_key_pair, first_note_pitch,
                          first_note_length):
    """This function takes all of the data received in service 1,
    and bundles it into a convenient JSON package.
    Keyword Arguments:
        key: The musical key, returned from our s1 form.
        time_signature: The time signature, as a tuple, from our s1 form.
        tempo: The tempo as int, from our s1 form.
        file_name: The file name as string, from our s1 form.
        scale_key_pair: The scale key pair, from our s1 form.
        rhythm_key_pair: The  rhythm key pair, from our s1 form.
        first_note_pitch: The first note pitch, from S2.
        first_note_length: The first note length, from S3.
    """

    service1_dictionary = {
        "key": key,
        "time_signature": time_signature,
        "tempo": tempo,
        "file_name": file_name,
        "scale_key_pair": scale_key_pair,
        "rhythm_key_pair": rhythm_key_pair,
        "first_note_pitch": first_note_pitch,
        "first_note_length": first_note_length
    }

    return service1_dictionary


def validate_on_submit_func(homepage_form):
    """This function executes logic for creating a JSON dictionary for all
    values, ready to be shipped onto service 4.

    Keyword Values:
        homepage_form: The form on our homepage.
    """

    service_2_url = service1.config['SERVICE_2_URL']
    service_3_url = service1.config['SERVICE_3_URL']

    # Retrieve the S2 dictionary with at GET request.
    s2_dict = get_service_2_response(service_2_url)

    # Convert the data from our form ready for JSON output.

    s2_post_data = convert_form_to_full_json_output(
        homepage_form.musical_scale.data,
        s2_dict)

    # Send post request to service 2 and get response.
    s2_post_resp = post_service_2_response(service_2_url, s2_post_data)

    print(f"s2_post_resp = {s2_post_resp}")

    s3_dict = get_service_3_response(service_3_url)

    s3_post_data = convert_form_to_full_json_output(
        homepage_form.rhythm_length.data,
        s3_dict)

    s3_post_resp = post_service_3_response(service_3_url, s3_post_data)

    print(f"s3_post_resp = {s3_post_resp}")

    s1_data = service_1_json_bundle(
        homepage_form.musical_key.data,
        homepage_form.time_signature.data,
        homepage_form.tempo.data,
        homepage_form.file_name.data,
        s2_post_data,
        s3_post_data,
        s2_post_resp,
        s3_post_resp)

    print("\n ----- s1_data ----- \n")

    print(s1_data)

    print("\n ----- End of s1_data ----- \n")

    return s1_data
