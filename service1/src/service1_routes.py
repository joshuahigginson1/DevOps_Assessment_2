"""This script contains all of our service 1 routes & endpoints."""

# Imports --------------------------------------------------------------

import requests
from flask import render_template, send_from_directory, abort

from src.service1_init import service1

from src.service1_logic import validate_on_submit_func, \
    get_midi_download_name, get_png_download_name, random_download_text,\
    listify, service_1_json_bundle, convert_form_to_full_json_output, \
    get_service_3_response, get_service_2_response


# Cache Control --------------------------------------------------------


@service1.after_request
def add_header(r):
    """ The add_header wrapper 'hijacks' our send_files request,
    and deliberately adds a number of headers to prevent our browser from
    caching our file output.

    Keyword Arguments:
        r: a request response.
    """

    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


# Routes ---------------------------------------------------------------

@service1.route("/", methods=["GET", "POST"])
def return_form():
    from src.service1_forms import MelodieForm

    homepage_form = MelodieForm()  # Instantiate a new form.

    service_4_url = service1.config["SERVICE_4_URL"]

    if homepage_form.validate_on_submit():
        json_data = validate_on_submit_func(homepage_form)
        our_file = requests.post(service_4_url, json=json_data, timeout=20)

        # Find the file name from user form.

        file_name = homepage_form.file_name.data

        png_download_name = get_png_download_name(file_name)
        midi_download_name = get_midi_download_name(file_name)

        file_dir = service1.config['FILES_DIRECTORY']

        png_file_dir = f"{file_dir}{png_download_name}"
        midi_file_dir = f"{file_dir}{midi_download_name}"

        # Gets the content type from the header of S4 response.

        if our_file.status_code == 200:

            s4_content_type = our_file.headers.get("Content-Type")

            # Then we write the file dependent on content type.

            if "png" in s4_content_type:  # MIDI File

                with open(png_file_dir, "wb") as file_to_write:
                    print("Writing bytes from service4 to new png file in "
                          "service1... \n")

                    file_to_write.write(our_file.content)
                    print("Written new file. \n")

                download_name = png_download_name

            else:  # Writes MIDI file.
                with open(midi_file_dir, "wb") as file_to_write:
                    print("Writing bytes from service4 to new midi file in "
                          "service1... \n")

                    file_to_write.write(our_file.content)
                    print("Written new file. \n")

                download_name = midi_download_name

            dl_text = random_download_text()

            return render_template('main_page_download.html',
                                   title=' ~ Download Ready! 🎶',
                                   form=homepage_form,
                                   download=download_name,
                                   dl_text=dl_text)

        else:

            # TODO: Add a flash message to user.
            print("There has been an error. File not saved.")

    return render_template('main_page.html',
                           title=' ~ Mélodie 🎶',
                           form=homepage_form)


@service1.route("/<download_name>", methods=["GET"])
def download_file(download_name):
    """This function downloads our file upon post request."""

    files_directory = service1.config["FILES_DIRECTORY"]

    print(f" The file directory is: {files_directory}")
    print(f" The filename is: {download_name}")

    try:
        return send_from_directory(files_directory,
                                   filename=download_name,
                                   as_attachment=True)

    except FileNotFoundError:
        abort(404)
