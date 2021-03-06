"""This script contains our logic for service 4"""

# Imports --------------------------------------------------------------
from os import environ

from flask import abort, send_from_directory
from mingus.containers import Bar
from mingus.midi import midi_file_out
from mingus.extra import lilypond

from time import sleep

import requests

from src.service4_init import service4


# Global Variables -----------------------------------------------------


PNG_DIRECTORY = service4.config["PNG_DIRECTORY"]

print(f"s4 logic .png dir: {PNG_DIRECTORY}")

MIDI_DIRECTORY = service4.config["MIDI_DIRECTORY"]

print(f"s4 logic .mid dir: {MIDI_DIRECTORY}")


# Functions ------------------------------------------------------------

def create_bar(user_time_signature):
    """This function returns a new Mingus bar object.
    Keyword Arguments:
        user_time_signature: The user's selected time signature from service 1.
        """
    return Bar("C", user_time_signature)


def post_service2(url, scale_key_pair):
    """Using our existing user data from s1, we use this function to
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


def post_service3(url, rhythm_key_pair):
    """Using our existing user data from s1, we use this function to
    poll s3 with a post request for a new note length.

    Keyword Arguments:
        url: The url of service 3.
        rhythm_key_pair: A key pair rhythm list dictionary.

    """

    service_3_response = requests.post(url, json=rhythm_key_pair)
    json_response_data = service_3_response.json()
    status_code_response = service_3_response.status_code

    print("\n ----------- Service 3 POST Response ----------- \n")

    print(f'Data: {json_response_data}')
    print(f'Response Code: {status_code_response}')

    print("\n ----------- End of Service 3 POST Response ----------- \n")

    return json_response_data


def initialise_bar(bar_object, note_length, note_pitch):
    """This function adds a new note to an existing bar object.
    Keyword Arguments:
        bar_object: Our empty mingus bar object.
        note_length: A given note length in mingus syntax.
        note_pitch: A given note pitch in mingus syntax.
        """

    if note_pitch == "r":
        return bar_object.place_rest(note_length)

    # If note is note, we call function place_notes().
    else:
        return bar_object.place_notes(note_pitch, note_length)


def add_notes_to_bar(initialised_bar,
                     s2_url,
                     s3_url,
                     scale_key_pair,
                     rhythm_key_pair):
    """
    This function fills an existing bar object with new notes, polled
    from service 2 and service 3.
    """

    while not initialised_bar.is_full():
        # ... we poll service 2 and 3 for a new note, and add to bar.

        new_note_pitch = post_service2(s2_url, scale_key_pair)
        print(f"The new note pitch is: {new_note_pitch}")

        new_note_length = post_service3(s3_url, rhythm_key_pair)
        print(f"The new note length is: {new_note_length}")

        initialise_bar(initialised_bar, new_note_length, new_note_pitch)

        # We need to set a sleep value, otherwise docker thinks that the
        # service is being DDOS'ed and actively refuses a connection.

        # sleep(0.3)

        print(initialised_bar)

    # When the bar is full, break out loop. It will return a full bar.

    print("\n ---------- THE BAR HAS BEEN FILLED ---------- \n")

    return "The bar has been filled!"


def overwrite_transpose_bar(bar, key_to_transpose):
    """This function transposes our full bar, dependent on the user's
    chosen key signature in service 1."""

    print(f'\nTransposing our file by {key_to_transpose} semitones...\n')

    if key_to_transpose != 0:
        return bar

    else:
        for note_container in bar:
            if note_container[2] is not None:
                note_container[2].transpose(key_to_transpose, True)

        return bar


def save_as_midi(file_name, output_bar, user_tempo):
    """This file generates a midi file from our mingus bar.

        Keyword Arguments:
            file_name: The user's chosen file name.midi
            output_bar: A full mingus bar.
            user_tempo: The user's selected tempo in BPM.
    """
    midi_file_suffix = file_name + "-melodie.mid"
    midi_save_location = f"{MIDI_DIRECTORY}{midi_file_suffix}"

    print(f'The .mid save location is: {midi_save_location} \n')

    return midi_file_out.write_Bar(midi_save_location, output_bar,
                                   user_tempo)


def save_as_png(file_name, output_bar):
    """This file generates a lilypond string from our mingus bar, and saves
    it as a PNG file.

        Keyword Arguments:
            file_name: The user's chosen file name.png
            output_bar: A full mingus bar.
    """
    lilypond_string = lilypond.from_Bar(output_bar, showkey=True,
                                        showtime=True)

    print('\n ---------- THE FILE HAS BEEN SAVED AS LILYPOND ---------- \n')

    print(f"The lilypond string is: {lilypond_string}\n")

    # This feature will only work with lilypond in path.

    png_file_suffix = file_name + "-melodie.png"

    png_save_location = f"{PNG_DIRECTORY}{png_file_suffix}"

    print(f'The .png save location is: {png_save_location} \n')

    return lilypond.to_png(lilypond_string, png_save_location)


def send_png_to_user(user_file_name):
    """This function returns our png file to the user if it has saved
    correctly.

     Keyword Arguments:
         user_file_name: The file name set by our user in service 1.
         """

    png_directory = service4.config["PNG_DIRECTORY"]

    print(f"Check PNG dir before sending: {png_directory}")

    print('\n ---------- THE PNG FILE IS SENDING... ---------- \n')

    try:
        print("I am trying to send the file... \n")

        return send_from_directory(png_directory,
                                   filename=user_file_name,
                                   as_attachment=False)

    except FileNotFoundError:

        print("THE FILE COULD NOT BE FOUND.")
        abort(404)


def send_midi_to_user(user_file_name):
    """This function returns our midi file to the user if it has saved
    correctly.

     Keyword Arguments:
         user_file_name: The file name set by our user in service 1.

         """

    midi_directory = service4.config["MIDI_DIRECTORY"]

    print(f"Check MIDI dir before sending: {midi_directory}")

    print('\n ---------- THE MIDI FILE IS SENDING... ---------- \n')

    try:

        print("I am trying to send the file... \n")

        return send_from_directory(midi_directory,
                                   filename=user_file_name,
                                   as_attachment=False)

    except FileNotFoundError:
        print("THE FILE COULD NOT BE FOUND.")
        abort(404)
