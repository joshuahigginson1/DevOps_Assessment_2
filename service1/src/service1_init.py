"""This file initialises our service 1 app."""

# Import Flask ---------------------------------------------------------

from os import environ

from flask import Flask

from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy

# Create Flask App -----------------------------------------------------

service1 = Flask(__name__)

if environ.get("FLASK_ENV") == 'production':
    service1.config.from_object('service1_config.ProductionConfig')

elif environ.get("FLASK_ENV") == 'testing':
    service1.config.from_object('service1_config.TestingConfig')

else:
    service1.config.from_object('service1_config.DevelopmentConfig')

# Import Routes --------------------------------------------------------

print(f"The SQLALCHEMY DATABASE URI IS: {service1.config['SQLALCHEMY_DATABASE_URI']}")

bootstrap = Bootstrap(service1)
db = SQLAlchemy(service1)

import src.service1_routes