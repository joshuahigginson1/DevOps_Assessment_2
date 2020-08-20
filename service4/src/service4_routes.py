"""This script contains our service4 routes."""

# Imports --------------------------------------------------------------

from flask import request

# Import our application.
from service4.src.service4_init import service4

# Import our Logic
from src.service4_logic import create_bar, initialise_bar, add_notes_to_bar,\
    transpose_bar, save_as_png, save_as_midi, send_png_to_user,\
    send_midi_to_user

# Import AST to perform literal evaluation.
import ast

# Global Variables -----------------------------------------------------


PNG_DIRECTORY = "/Users/mac/Documents/GitHub/DevOps_Assessment_2/src" \
                "/service4/png_output/"

MIDI_DIRECTORY = "/Users/mac/Documents/GitHub/DevOps_Assessment_2/src" \
                 "/service4/midi_output/"

SERVICE_2_URL = "http://0.0.0.0:5002/"
SERVICE_3_URL = "http://0.0.0.0:5003/"


# Routes ---------------------------------------------------------------

@service4.route("/", methods=["POST"])
def service4_post_request():
    """This function triggers on a post request to service 4."""

    # When we get a post request from S1, we first take the data and unpack it
    # into something useful to us.

    s1_data = request.get_json()
    print(f"Received from S1: {s1_data}")

    # We create a new bar with this information.

    encode_time_signature = s1_data.get("time_signature")
    decode_time_signature = ast.literal_eval(encode_time_signature)

    new_bar = create_bar(decode_time_signature)

    # Then we initialise the bar.

    print(" \n ----- Note Before Initialisation ----- \n")

    print(new_bar)

    initialise_bar(new_bar,
                   s1_data.get("first_note_length"),
                   s1_data.get("first_note_pitch"))

    print(" \n ----- Note After Initialisation ----- \n")

    print(new_bar)

    # We run our "poll s2 and s3" function to fill the bar.

    scale_key_pair = s1_data.get("scale_key_pair")

    rhythm_key_pair = s1_data.get("rhythm_key_pair")

    # Keep adding notes to our bar.

    add_notes_to_bar(new_bar, SERVICE_2_URL,
                     SERVICE_3_URL, scale_key_pair, rhythm_key_pair)

    print(" \n ----- Note after S2 S3 Polling ----- \n ")

    print(new_bar)

    # We transpose the bar.

    # transpose_bar(new_bar, s1_data.get("key"))

    # print(f"Transposed bar: {new_bar}")

    # === IF MIDI! ===

    save_as_midi(s1_data.get("file_name"), new_bar, s1_data.get("tempo"))

    # Send midi file name to user.

    return send_midi_to_user(s1_data.get("file_name",), MIDI_DIRECTORY)

    # === IF PNG! ===

    # save_as_png(s1_data.get("file_name"), new_bar)

    # Send png file name to user.

    # return send_png_to_user(s1_data.get("file_name"), PNG_DIRECTORY)
