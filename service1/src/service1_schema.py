"""This script represents our SQL database model."""

# Imports --------------------------------------------------------------

from src.service1_init import db


# Classes---------------------------------------------------------------

class Downloads(db.Model):
    """A class that represents a download of our file."""
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    file_name = db.Column(db.String(30), nullable=False)
    musical_key = db.Column(db.String(200), nullable=False)
    musical_scale = db.Column(db.String(200), nullable=False)
    rhythm_length = db.Column(db.String(200), nullable=False)
    tempo = db.Column(db.Integer, nullable=False)
    time_signature = db.Column(db.String(20), nullable=False)

    def __repr__(self):  # Define the self representation of our data.
        return f"Download ID: {str(self.id)},\n" \
               f"Date Created: {str(self.date)},\n" \
               f"File Name: {self.file_name},\n" \
               f"Musical Key: {self.musical_key},\n" \
               f"Musical Scale: {self.musical_scale},\n" \
               f"Rhythm Length: {self.rhythm_length},\n" \
               f"Tempo: {str(self.tempo)},\n" \
               f"Time Signature: {self.time_signature}"
