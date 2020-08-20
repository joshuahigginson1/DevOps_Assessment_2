# Task:

# Imports --------------------------------------------------------------

import requests
from flask import render_template, send_from_directory, abort



@service1.after_request
def add_header(r):
    """
    Add headers to force delete our cache.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


# Routes ---------------------------------------------------------------

@service1.route("/", methods=["GET", "POST"])
def return_form():
    from src import MelodieForm

    homepage_form = MelodieForm()  # Instantiate a new form.

    service_4_url = "http://0.0.0.0:5004"

    if homepage_form.validate_on_submit():
        json_data = validate_on_submit_func(homepage_form)
        our_file = requests.post(service_4_url, json=json_data)

        # Find the file name from user form.

        file_name = homepage_form.file_name.data

        png_download_name = get_png_download_name(file_name)
        midi_download_name = get_midi_download_name(file_name)
        png_file_dir = f"service1/src/file_output/{png_download_name}"
        midi_file_dir = f"service1/src/file_output/{midi_download_name}"

        # Gets the content type from the header of S4 response.

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

        return render_template('main_page_download.html',
                               title='🎶 ~ Download Ready! ~ 🎶',
                               form=homepage_form,
                               download=download_name)

    return render_template('main_page.html',
                           title='🎶 ~ Mélodie ~ 🎶',
                           form=homepage_form)


@service1.route("/<download_name>", methods=["GET", "POST"])
def download_png(download_name):
    """This function downloads our file upon post request."""

    files_directory = "/Users/mac/Documents/GitHub/DevOps_Assessment_2/src" \
                      "/service1/file_output/"

    print(f" The file directory is: {files_directory}")
    print(f" The filename is: {download_name}")

    try:
        return send_from_directory(files_directory,
                                   filename=download_name,
                                   as_attachment=True)

    except FileNotFoundError:
        abort(404)


# Run Service ----------------------------------------------------------

if __name__ == "__main__":
    service1.run(port=5001)
