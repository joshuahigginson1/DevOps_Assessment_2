"""
A template which lays out the basic syntax for a service1_forms.py file with WTForms.
"""

# Imports --------------------------------------------------------------

from flask_wtf import FlaskForm  # Import our Flask Form.
from wtforms import StringField, SelectField, SubmitField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired, Length, NumberRange, \
    ValidationError

from service1.src.service1_logic import get_service_2_response,\
    get_service_3_response

from service1.src.service1_init import service1

# Classes --------------------------------------------------------------


class MelodieForm(FlaskForm):

    """This is the main form for the front page of service 1."""

    service_2_url = service1.config["SERVICE_2_URL"]
    service_3_url = service1.config["SERVICE_3_URL"]

    """ Our list gets sent backwards. We need to reverse it to display 
    correctly in our form. """

    forward_s2_list = list(get_service_2_response(service_2_url).items())
    bward_s2_list = [(value, key) for (key, value) in forward_s2_list]

    forward_s3_list = list(get_service_3_response(service_3_url).items())
    bward_s3_list = [(value, key) for (key, value) in forward_s3_list]

    file_name = StringField('File Name: ', validators=[

                                DataRequired(
                                    message="Please enter a file name."),

                                Length(message="File names should be between "
                                               "between 4 and 30 characters.",
                                       min=4,
                                       max=30)])

    musical_key = SelectField('Key Root: ',
                              default=(0, 'C'),
                              choices=[
                                  (0, 'C'),
                                  (1, 'C#'),
                                  (1, 'Db'),
                                  (2, 'D'),
                                  (3, 'D#'),
                                  (3, 'Eb'),
                                  (4, 'E'),
                                  (5, 'F'),
                                  (6, 'F#'),
                                  (6, 'Gb'),
                                  (7, 'G'),
                                  (8, 'G#'),
                                  (8, 'Ab'),
                                  (9, 'A'),
                                  (10, 'A#'),
                                  (10, "Bb"),
                                  (11, "B")
                              ],
                              validators=[
                                  DataRequired(message="Please pick a key.")])

    # Get Musical Scale info from get request to service 2.

    musical_scale = SelectField('Scale: ',
                                choices=bward_s2_list,

                                default=[1, 2, 3, 4, 5, 6, 7, 8,
                                         9, 10, 11, 12, "r"],

                                validators=[
                                    DataRequired(message="Pick a scale.")])

    # Get list of rhythms using a get request to service 3.

    rhythm_length = SelectField("Rhythm: ",
                                choices=bward_s3_list,

                                default=[2, 4, 8, 16],

                                validators=[
                                    DataRequired(message="Pick a rhythm.")])

    tempo = IntegerRangeField('Tempo: ',
                              default=120,
                              validators=[NumberRange(min=60, max=220)])

    time_signature = SelectField('Time Signature: ',
                                 default=((4, 4), "4/4"),
                                 choices=[
                                     ((4, 4), "4/4"),
                                     ((3, 4), "3/4"),
                                     ((2, 4), "2/4"),
                                     ((5, 4), "5/4"),
                                     ((6, 8), "6/8"),
                                     ((12, 8), "12/8")
                                 ],
                                 validators=[DataRequired(
                                     message="Pick a time signature.")])

    go = SubmitField("Let's go!")

    # Custom Validators ------------------------------------------------

    def validate_file_name(self, file_name):
        cannot_contain = ["/", ".", "{", "}", "[", "]", "=", "$"]
        for character in cannot_contain:
            if character in file_name.data:
                raise ValidationError(
                    'Your file name contains illegal characters.')
