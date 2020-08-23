"""This file initialises our service 4 app."""

# Import Flask ---------------------------------------------------------

from os import environ
from flask import Flask


# Create Flask App -----------------------------------------------------

service4 = Flask(__name__)

if environ.get("FLASK_ENV") == 'production':
    service4.config.from_object('service4_config.ProductionConfig')

elif environ.get("FLASK_ENV") == 'testing':
    service4.config.from_object('service4_config.TestingConfig')

else:
    service4.config.from_object('service4_config.DevelopmentConfig')


# Import Routes --------------------------------------------------------

import src.service4_routes
