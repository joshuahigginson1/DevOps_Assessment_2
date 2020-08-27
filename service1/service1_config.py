"""Config file for service 1."""

# imports ------------------------------

from os import environ, path

# .env location ------------------------

# We find the absolute path of the root directory of our current file.
basedir = path.abspath(path.dirname(__file__))


# Declare Classes ------------------------------------------------------

class Config(object):  # General Config

    FLASK_APP = 'service1_wsgi.py'

    DEBUG = False
    TESTING = False

    FILES_DIRECTORY = path.join(basedir, environ.get('FILES_DIRECTORY'))

    SECRET_KEY = environ.get("PRODUCTION_SECRET_KEY")

    SERVICE_2_URL = "0.0.0.0:5002"
    SERVICE_3_URL = "0.0.0.0:5003"
    SERVICE_4_URL = "0.0.0.0:5004"


class ProductionConfig(Config):

    ENV = 'production'

    DB_USER = environ.get('PRODUCTION_DB_USERNAME')
    DB_PASS = environ.get('PRODUCTION_DB_USERPASS')
    DB_ADD = environ.get('PRODUCTION_DATABASE_ADDRESS')
    DB_NAME = environ.get('PRODUCTION_DB')

    DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADD}/{DB_NAME}"

    SERVICE_2_URL = environ.get('SERVICE_2_URL')
    SERVICE_3_URL = environ.get('SERVICE_3_URL')
    SERVICE_4_URL = environ.get('SERVICE_4_URL')

class DevelopmentConfig(Config):
    DEBUG = True

    ENV = 'development'

    DB_USER = environ.get('DEVELOPMENT_DB_USERNAME')
    DB_PASS = environ.get('DEVELOPMENT_DB_USERPASS')
    DB_ADD = environ.get('DEVELOPMENT_DATABASE_ADDRESS')
    DB_NAME = environ.get('DEVELOPMENT_DB')

    DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADD}/{DB_NAME}"

    SECRET_KEY = environ.get("DEV_SECRET_KEY")


class TestingConfig(Config):
    TESTING = True

    ENV = 'testing'

    DB_USER = environ.get('TESTING_DB_USERNAME')
    DB_PASS = environ.get('TESTING_DB_USERPASS')
    DB_ADD = environ.get('TESTING_DATABASE_ADDRESS')
    DB_NAME = environ.get('TESTING_DB')

    DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADD}/{DB_NAME}"

    SECRET_KEY = environ.get("TESTING_SECRET_KEY")
