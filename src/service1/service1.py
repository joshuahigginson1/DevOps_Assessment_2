# Task:

# Imports --------------------------------------------------------------

import requests
from flask import Flask, jsonify

# Flask ----------------------------------------------------------------

# Create our flask application.
service1 = Flask(__name__)

# Functions ------------------------------------------------------------


def get_service_2_response(url):
    """This function returns a get response from service 2."""
    # TODO: Add s2 get response test.
    service_2_response = requests.get(url)
    decoded_service_2_response = service_2_response.json()

    print("\n ----------- Service 2 GET Response ----------- \n")
    print(decoded_service_2_response)

    return decoded_service_2_response


def get_service_3_response(url):
    """This function returns a get request from service 3."""
    # TODO: Add s3 get response test.
    service_3_response = requests.get(url)
    decoded_service_3_response = service_3_response.json()

    print("\n ----------- Service 3 GET Response ----------- \n")
    print(decoded_service_3_response)
    print("\n ----------- End of GET Responses ----------- \n")

    return decoded_service_3_response


def post_service_2_response(url):
    """This function returns a post request from service 2."""
    # TODO: Add s2 post response functionality & tests.
    return "hi"


def post_service_3_response(url):
    """This function returns a post request from service 2."""
    # TODO: Add s3 post response functionality & tests.
    return "hi"


# Methods --------------------------------------------------------------


# Define Variables -----------------------------------------------------


# Execute Code ---------------------------------------------------------

service_2_url = "http://0.0.0.0:5002/"
service_3_url = "http://0.0.0.0:5003/"

get_service_2_response(service_2_url)
get_service_3_response(service_3_url)

# Run Service ----------------------------------------------------------

if __name__ == "__main__":
    service1.run(port=5001)
