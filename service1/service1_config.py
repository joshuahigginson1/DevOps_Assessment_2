"""Config file for service 1."""

# imports ------------------------------

from os import environ, path
from dotenv import load_dotenv

# .env location ------------------------

# We find the absolute path of the root directory of our current file.
basedir = path.abspath(path.dirname(__file__))

# Load our specific .env file from the root directory of our current file.
load_dotenv(path.join(basedir, 'service1.env'))


# Declare Classes ------------------------------------------------------

class Config(object):  # General Config

    FLASK_APP = 'service1_wsgi.py'

    DEBUG = False
    TESTING = False

    FILES_DIRECTORY = f"{basedir}{environ.get('FILES_DIRECTORY')}"

    SERVICE_2_URL = environ.get("SERVICE_2_URL")
    SERVICE_3_URL = environ.get("SERVICE_3_URL")
    SERVICE_4_URL = environ.get("SERVICE_4_URL")

    SECRET_KEY = environ.get("PRODUCTION_SECRET_KEY")


class ProductionConfig(Config):

    ENVIRONMENT = 'production'

    pass


class DevelopmentConfig(Config):
    DEBUG = True

    ENVIRONMENT = 'development'

    SECRET_KEY = environ.get("DEV_SECRET_KEY")


class TestingConfig(Config):
    TESTING = True

    ENVIRONMENT = 'testing'

    SECRET_KEY = environ.get("TESTING_SECRET_KEY")
