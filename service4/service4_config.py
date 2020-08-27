# imports ------------------------------

from os import environ, path

# .env location ------------------------

# We find the absolute path of the root directory of our current file.
basedir = path.abspath(path.dirname(__file__))

print(f"The basedir is: {basedir} \n")


# Declare Classes ------------------------------------------------------

class Config(object):  # General Config

    FLASK_APP = 'service4_wsgi.py'

    DEBUG = False
    TESTING = False

    PNG_DIRECTORY = path.join(basedir, environ.get('PNG_DIRECTORY'))
    MIDI_DIRECTORY = path.join(basedir, environ.get('MIDI_DIRECTORY'))

    print(f"The PNG_DIR is: {PNG_DIRECTORY}")
    print(f"The MIDI_DIR is: {PNG_DIRECTORY}")

    SERVICE_2_URL = environ.get("SERVICE_2_URL")
    SERVICE_3_URL = environ.get("SERVICE_3_URL")


class ProductionConfig(Config):

    ENV = 'production'


class DevelopmentConfig(Config):

    ENV = 'development'

    DEBUG = True


class TestingConfig(Config):

    ENV = 'testing'

    TESTING = True
