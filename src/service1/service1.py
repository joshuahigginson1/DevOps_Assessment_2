# Task:

# Imports --------------------------------------------------------------

import requests
from flask import Flask, jsonify, render_template

# Flask ----------------------------------------------------------------

# Create our flask application.

service1 = Flask(__name__)
service1.config['SECRET_KEY'] = "selrkgjshglkjhgv345ksdhke4tdg"

# Functions ------------------------------------------------------------


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
    print(list_of_dict_items)

    for label, value in list_of_dict_items:
        print(f"labeltype: {type(label)}")
        print(f"{label}\n \n")
        print(f"valuetype: {type(value)}")
        print(f"{value}\n \n")
        print(f"validformtype: {type(form_get_on_validation[0])}")
        print(f"{form_get_on_validation} \n \n")

        if value == form_get_on_validation:
            print("I am an idiot sandwich.")


def get_service_2_response(url):
    """This function returns a get response from service 2."""
    # TODO: Add s2 get response test.
    service_2_response = requests.get(url)
    decoded_service_2_response = service_2_response.json()

    print("\n ----------- Service 2 GET Response ----------- \n")
    print(decoded_service_2_response)
    print("\n ----------- End of Service 2 GET Response ----------- \n")
    return decoded_service_2_response

# Now, we need to find a way of using this in our form.


def get_service_3_response(url):
    """This function returns a get request from service 3."""
    # TODO: Add s3 get response test.
    service_3_response = requests.get(url)
    decoded_service_3_response = service_3_response.json()

    print("\n ----------- Service 3 GET Response ----------- \n")
    print(decoded_service_3_response)
    print("\n ----------- End of Service 3 GET Response ----------- \n")

    return decoded_service_3_response

# Now, we need to find a way of using this in our form.


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


def post_service_3_response(url, data):
    """This function returns a post request from service 2."""
    # TODO: Add s3 post response functionality & tests.
    return "hi"


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
        "time_signature": (4, 4),  # From Service #1
        "tempo": tempo,
        "file_name": file_name,
        "scale_key_pair": {"major blues": [1, 3, 4, 5, 8, 10, "r"]},
        "rhythm_key_pair": {"standard": [1, 2, 4, 8, 16, 32]},

        "first_note_pitch": "C",  # Pull a note pitch from service #2.
        "first_note_length": 6,  # Pull a note length from service #3.
    }

    return jsonify(service1_dictionary)


# Routes ---------------------------------------------------------------

@service1.route("/", methods=["GET", "POST"])
def return_form():

    from src.service1.forms import MelodieForm
    homepage_form = MelodieForm()  # Instantiate a new form.

    service_2_url = "http://0.0.0.0:5002/"
    service_3_url = "http://0.0.0.0:5003/"

    if homepage_form.validate_on_submit():

        # post_service_2_response(service_2_url)
        # post_service_3_response(service_3_url, data)

        s2_dict = get_service_2_response(service_2_url)

        aa = homepage_form.musical_scale.raw_data
        print(convert_form_to_full_json_output(aa, s2_dict))


        # s1_data = service_1_json_bundle(
        #    homepage_form.musical_key.data,
        #    homepage_form.time_signature.data,
        #    homepage_form.tempo.data,
        #    homepage_form.file_name.data)
        # return #Something

    return render_template('main_page.html', title='🎶 ~ Mélodie ~ 🎶',
                           form=homepage_form)

# Run Service ----------------------------------------------------------

if __name__ == "__main__":
    service1.run(port=5001)
