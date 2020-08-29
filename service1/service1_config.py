"""Config file for service 1."""

# imports ------------------------------

from os import environ, path, getenv

# .env location ------------------------

# We find the absolute path of the root directory of our current file.
basedir = path.abspath(path.dirname(__file__))


# Functions ------------------------------------------------------------

def remove_quotes(string):
    """ This function removes any speech mark quotes from a string input.

        Keyword Arguments;
            string: A string with speech marks.
    """

    return string.replace('"', '')


# Declare Classes ------------------------------------------------------

class Config(object):  # General Config

    FLASK_APP = 'service1_wsgi.py'

    DEBUG = False
    TESTING = False

    files_dir_env = remove_quotes(environ.get("FILES_DIRECTORY"))

    FILES_DIRECTORY = path.join(basedir, files_dir_env)

    SECRET_KEY = remove_quotes(environ.get("PRODUCTION_SECRET_KEY"))

    SERVICE_2_URL = remove_quotes(environ.get('SERVICE_2_URL'))
    SERVICE_3_URL = remove_quotes(environ.get('SERVICE_3_URL'))
    SERVICE_4_URL = remove_quotes(environ.get('SERVICE_4_URL'))

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):

    ENV = 'production'

    DB_USER = environ.get('PRODUCTION_DB_USERNAME')
    DB_PASS = environ.get('PRODUCTION_DB_USERPASS')
    DB_ADD = environ.get('PRODUCTION_DATABASE_ADDRESS')
    DB_NAME = environ.get('PRODUCTION_DB')

    database_step_1 = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADD}/{DB_NAME}"

    SQLALCHEMY_DATABASE_URI = str(remove_quotes(database_step_1))


class DevelopmentConfig(Config):
    DEBUG = True

    ENV = 'development'

    DB_USER = environ.get('DEVELOPMENT_DB_USERNAME')
    DB_PASS = environ.get('DEVELOPMENT_DB_USERPASS')
    DB_ADD = environ.get('DEVELOPMENT_DATABASE_ADDRESS')
    DB_NAME = environ.get('DEVELOPMENT_DB')

    database_step_1 = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADD}/{DB_NAME}"

    SQLALCHEMY_DATABASE_URI = str(remove_quotes(database_step_1))

    SECRET_KEY = remove_quotes(environ.get("DEV_SECRET_KEY"))


class TestingConfig(Config):
    TESTING = True

    ENV = 'testing'

    DB_USER = environ.get('TESTING_DB_USERNAME')
    DB_PASS = environ.get('TESTING_DB_USERPASS')
    DB_ADD = environ.get('TESTING_DATABASE_ADDRESS')
    DB_NAME = environ.get('TESTING_DB')

    database_step_1 = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADD}/{DB_NAME}"

    SQLALCHEMY_DATABASE_URI = str(remove_quotes(database_step_1))

    SECRET_KEY = remove_quotes(environ.get("TESTING_SECRET_KEY"))
