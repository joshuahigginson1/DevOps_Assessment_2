# imports ------------------------------

from os import environ, path

# Find the absolute path of the root directory of our current file. ----

basedir = path.abspath(path.dirname(__file__))

print(f"The basedir is: {basedir} \n")

# Functions ------------------------------------------------------------

def remove_quotes(string):
    """ This function removes any speech mark quotes from a string input.

        Keyword Arguments;
            string: A string with speech marks.
    """

    return string.replace('"', '')

# Declare Classes ---
# ---------------------------------------------------

class Config(object):  # General Config

    FLASK_APP = 'service4_wsgi.py'

    DEBUG = False
    TESTING = False

    PNG_DIRECTORY = path.join(basedir, remove_quotes(environ.get(
        'PNG_DIRECTORY')))

    MIDI_DIRECTORY = path.join(basedir, remove_quotes(environ.get(
        'MIDI_DIRECTORY')))

    print(f"The PNG_DIR is: {PNG_DIRECTORY}")
    print(f"The MIDI_DIR is: {PNG_DIRECTORY}")

    SERVICE_2_URL = "http://0.0.0.0:5002"
    SERVICE_3_URL = "http://0.0.0.0:5003"


class ProductionConfig(Config):

    ENV = 'production'

    SERVICE_2_URL = remove_quotes(environ.get("SERVICE_2_URL"))
    SERVICE_3_URL = remove_quotes(environ.get("SERVICE_3_URL"))


class DevelopmentConfig(Config):

    ENV = 'development'

    DEBUG = True


class TestingConfig(Config):

    ENV = 'testing'

    TESTING = True
