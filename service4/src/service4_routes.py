"""This script contains our service4 routes."""

# Imports --------------------------------------------------------------

from flask import request

# Import our application.
from src.service4_init import service4

# Import our Logic
from src.service4_logic import create_bar, initialise_bar, add_notes_to_bar,\
    save_as_png, save_as_midi, send_png_to_user,\
    send_midi_to_user, overwrite_transpose_bar

# Import AST to perform literal evaluation.
import ast

from os import environ

# Global Variables -----------------------------------------------------


PNG_DIRECTORY = service4.config["PNG_DIRECTORY"]

print(f"s4 routes .png dir: {PNG_DIRECTORY}")

MIDI_DIRECTORY = service4.config["MIDI_DIRECTORY"]

print(f"s4 routes .mid dir: {MIDI_DIRECTORY}")

SERVICE_2_URL = service4.config["SERVICE_2_URL"]
SERVICE_3_URL = service4.config["SERVICE_3_URL"]


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

    print(" \n ----- THE BAR IS FULL ----- \n ")

    print(new_bar)

    # We transpose the bar.

    overwrite_transpose_bar(new_bar, s1_data.get("key"))

    print(f"Transposed bar: {new_bar}")

    # === IF MIDI! ===

    # save_as_midi(s1_data.get('file_name'), new_bar, s1_data.get("tempo"))

    # print('\n ---------- THE FILE HAS BEEN SAVED AS MIDI ---------- \n')

    # Send midi file name to user.

    # midi_file_name = f"{s1_data.get('file_name')}-melodie.mid"

    # return send_midi_to_user(midi_file_name)

    # === IF PNG! ===

    png_file_name = f"{s1_data.get('file_name')}-melodie.png"

    save_as_png(s1_data.get("file_name"), new_bar)

    print('\n ---------- THE FILE HAS BEEN SAVED AS PNG ---------- \n')

    return send_png_to_user(png_file_name)
