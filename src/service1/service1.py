# Task:

# Imports --------------------------------------------------------------
import ast

import requests
from flask import Flask, render_template

# Flask ----------------------------------------------------------------

# Create our flask application.

service1 = Flask(__name__)
service1.config['SECRET_KEY'] = "selrkgjshglkjhgv345ksdhke4tdg"


# Functions ------------------------------------------------------------


def listify(input_string):
    """This method converts our string representation of a list,
    to an actual list."""
    input_string = ast.literal_eval(input_string)
    return input_string


def convert_form_to_full_json_output(form_get_on_validation, full_dict):
    """This is a helper function for our forms.
    Our forms can only return one part of our dictionary. Here, we do a
    lookup, retrieve the other half of the key-value pair, then stick them
    back together in a python dictionary, ready for jsonification.
    Keyword Arguments:
        full_dict: A full python dictionary of every key-value pair.
        form_get_on_validation: The value from our user.

    """
    list_of_dict_items = list(full_dict.items())
    output_form_list = listify(form_get_on_validation)
    new_dict = {}

    for label, value in list_of_dict_items:
        if value == output_form_list:
            print("I am an NOT idiot sandwich. This works!")
            new_dict = {label: value}

    return new_dict


def get_service_2_response(url):
    """This function returns a get response from service 2."""
    # TODO: Add s2 get response test.
    service_2_response = requests.get(url)
    decoded_service_2_response = service_2_response.json()

    print("\n ----------- Service 2 GET Response ----------- \n")
    print(decoded_service_2_response)
    print("\n ----------- End of Service 2 GET Response ----------- \n")
    return decoded_service_2_response


def get_service_3_response(url):
    """This function returns a get request from service 3."""
    # TODO: Add s3 get response test.
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
    status_code_response = service_2_response.status_code

    print("\n ----------- Service 2 POST Response ----------- \n")

    print(f'Data: {json_response_data}')
    print(f'Response Code: {status_code_response}')

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


def post_service_4_response(url):
    """This function sends our collected data as post request to service 4."""
    pass


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
    values, ready to be shipped onto service 4."""

    service_2_url = "http://0.0.0.0:5002/"
    service_3_url = "http://0.0.0.0:5003/"

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

    print("\n ----- End of S1 Data ----- \n")

    return s1_data


# Routes ---------------------------------------------------------------

@service1.route("/", methods=["GET", "POST"])
def return_form():
    from src.service1.forms import MelodieForm
    homepage_form = MelodieForm()  # Instantiate a new form.

    if homepage_form.validate_on_submit():
        validate_on_submit_func(homepage_form)

    return render_template('main_page.html', title='🎶 ~ Mélodie ~ 🎶',
                           form=homepage_form)


# Run Service ----------------------------------------------------------

if __name__ == "__main__":
    service1.run(port=5001)
