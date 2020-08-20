"""This file initialises our service 1 app."""

# Import Flask ---------------------------------------------------------

from os import environ

from flask import Flask

# Create Flask App -----------------------------------------------------

service1 = Flask(__name__)

if environ.get("ENVIRONMENT") == 'production':
    service1.config.from_object('service1_config.ProductionConfig')

elif environ.get("ENVIRONMENT") == 'testing':
    service1.config.from_object('service1_config.TestingConfig')

else:
    service1.config.from_object('service1_config.DevelopmentConfig')

# Import Routes --------------------------------------------------------

from service1.src import service1_routes