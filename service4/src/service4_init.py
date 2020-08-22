"""This file initialises our service 4 app."""

# Import Flask ---------------------------------------------------------

from os import environ
from flask import Flask


# Create Flask App -----------------------------------------------------

service4 = Flask(__name__)

if environ.get("ENVIRONMENT") == 'production':
    service4.config.from_object('service4_config.ProductionConfig')

elif environ.get("ENVIRONMENT") == 'testing':
    service4.config.from_object('service4_config.TestingConfig')

else:
    service4.config.from_object('service4_config.DevelopmentConfig')

# Import Routes --------------------------------------------------------

import service4_routes
