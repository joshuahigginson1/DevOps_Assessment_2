"""Config file for service 2."""

# imports ------------------------------

from os import environ, path
from dotenv import load_dotenv

# .env location ------------------------

# We find the absolute path of the root directory of our current file.
basedir = path.abspath(path.dirname(__file__))

# Load our specific .env file from the root directory of our current file.
load_dotenv(path.join(basedir, 'service2.env'))


# Declare Classes ------------------------------------------------------

class Config(object):  # General Config

    FLASK_APP = 'service2_wsgi.py'

    DEBUG = False
    TESTING = False


class ProductionConfig(Config):

    ENV = 'production'


class DevelopmentConfig(Config):

    ENV = 'development'

    DEBUG = True


class TestingConfig(Config):

    ENV = 'testing'

    TESTING = True
