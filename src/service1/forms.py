"""
A template which lays out the basic syntax for a forms.py file with WTForms.
"""

# Imports --------------------------------------------------------------

from flask_wtf import FlaskForm  # Import our Flask Form.
from wtforms import StringField, SelectField, SubmitField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired, Length, NumberRange

# Classes --------------------------------------------------------------


class MelodieForm(FlaskForm):  # Creates child class from parent 'FlaskForm'.
    """This is the main form for our front page of service #1."""

    file_name = StringField('File Name',
                            default="melodie",
                            validators=[
                                DataRequired(
                                    message="Please enter a file name."),
                                Length(message="File names should be between "
                                               "between 4 and 30 characters.",
                                       min=4,
                                       max=30)])

    musical_key = SelectField('Key Root',
                              default='C',
                              choices=['C', 'C#', 'Db', 'D', 'D#',
                                       'Eb', 'E', 'F', 'F#', 'Gb',
                                       'G', 'G#', 'Ab', 'A',
                                       'A#', 'Bb', 'B'],
                              validators=[
                                  DataRequired(message="Please pick a key.")])

    # Get Musical Scale info from get request to service 2.

    musical_scale = SelectField('Scale',
                                default='minor blues',
                                choices=["chromatic",
                                         "major",
                                         "major pentatonic",
                                         "major blues",
                                         "natural minor",
                                         "harmonic minor",
                                         "minor pentatonic",
                                         "minor blues"],
                                validators=[
                                    DataRequired(message="Pick a scale.")])

    # Get list of rhythms using a get request to service 3.

    rhythm_length = SelectField("rhythm",
                                default='Rhythm of the night',
                                choices=["FROM SERVICE 3"],
                                validators=[
                                    DataRequired(message="Pick a rhythm.")])

    tempo = IntegerRangeField('Tempo',
                              default=120,
                              validators=[NumberRange(min=60, max=220)])

    time_signature = SelectField('Time Signature',
                                 default=(4, 4),
                                 choices=[(4, 4), (3, 4), (2, 4),
                                          (5, 4), (6, 8), (12, 8)],
                                 validators=[DataRequired(
                                     message="Pick a time signature.")])

    go = SubmitField('Go')
    refresh = SubmitField('Refresh')
