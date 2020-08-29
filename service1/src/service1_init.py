"""This file initialises our service 1 app."""

# Import Flask ---------------------------------------------------------

from os import environ, system

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

print(f"The DATABASE URI IS: {service1.config['SQLALCHEMY_DATABASE_URI']}")
print(f"The FILES DIR ENV IS: {environ.get('FILES_DIRECTORY')}")
print(f"The FILES DIR IS: {service1.config['FILES_DIRECTORY']}")

bootstrap = Bootstrap(service1)
db = SQLAlchemy(service1)

# Build Database Schema ------------------------------------------------

from src.service1_schema import Downloads

db.create_all()

import src.service1_routes
