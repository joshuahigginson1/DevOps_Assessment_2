"""
A template which lays out the basic syntax for a forms.py file with WTForms.
"""

# Imports --------------------------------------------------------------

from flask_wtf import FlaskForm  # Import our Flask Form.
from wtforms import StringField, SelectField, SubmitField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired, Length, NumberRange

from src.service1.service1 import get_service_2_response, \
    get_service_3_response


# Classes --------------------------------------------------------------

# We need to grab the json dictionary from service 2, and turn it into a
# list of tuples.

# hen you do dict.items() in python3, you return a
# 'dictionary_view object.


class MelodieForm(FlaskForm):  # Creates child class from parent 'FlaskForm'.

    """This is the main form for our front page of service #1."""

    service_2_url = "http://0.0.0.0:5002/"
    service_3_url = "http://0.0.0.0:5003/"

    """ Our list gets sent backwards. We need to reverse it to display 
    correctly in our form. """

    forward_s2_list = list(get_service_2_response(service_2_url).items())
    bward_s2_list = [(value, key) for (key, value) in forward_s2_list]

    forward_s3_list = list(get_service_3_response(service_3_url).items())
    bward_s3_list = [(value, key) for (key, value) in forward_s3_list]

    file_name = StringField('File Name',
                            default="my_first_melodie",
                            validators=[
                                DataRequired(
                                    message="Please enter a file name."),
                                Length(message="File names should be between "
                                               "between 4 and 30 characters.",
                                       min=4,
                                       max=30)])

    musical_key = SelectField('Key Root',
                              default=(1, 'C'),
                              choices=[
                                  (1, 'C'),
                                  (2, 'C#'),
                                  (2, 'Db'),
                                  (3, 'D'),
                                  (4, 'D#'),
                                  (4, 'Eb'),
                                  (5, 'E'),
                                  (6, 'F'),
                                  (7, 'F#'),
                                  (7, 'Gb'),
                                  (8, 'G'),
                                  (9, 'G#'),
                                  (9, 'Ab'),
                                  (10, 'A'),
                                  (11, 'A#'),
                                  (11, "Bb"),
                                  (12, "B")
                              ],
                              validators=[
                                  DataRequired(message="Please pick a key.")])

    # Get Musical Scale info from get request to service 2.

    musical_scale = SelectField('Scale',
                                choices=bward_s2_list,

                                default=[1, 2, 3, 4, 5, 6, 7, 8,
                                         9, 10, 11, 12, "r"],

                                validators=[
                                    DataRequired(message="Pick a scale.")])

    # Get list of rhythms using a get request to service 3.

    rhythm_length = SelectField("Rhythm",
                                choices=bward_s3_list,

                                default=[1, 2, 4, 8, 16, 32],

                                validators=[
                                    DataRequired(message="Pick a rhythm.")])

    tempo = IntegerRangeField('Tempo',
                              default=120,
                              validators=[NumberRange(min=60, max=220)])

    time_signature = SelectField('Time Signature',
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

    go = SubmitField('Go')
