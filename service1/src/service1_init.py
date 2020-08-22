"""This file initialises our service 1 app."""

# Import Flask ---------------------------------------------------------

from os import environ

from flask import Flask

from flask_bootstrap import Bootstrap

# Create Flask App -----------------------------------------------------

service1 = Flask(__name__)

print(f"The current environment is: {environ.get('ENV')}")

if environ.get("ENV") == 'production':
    service1.config.from_object('service1_config.ProductionConfig')

elif environ.get("ENV") == 'testing':
    service1.config.from_object('service1_config.TestingConfig')

else:
    service1.config.from_object('service1_config.DevelopmentConfig')

print(f"The service1 config mode is: {service1.config['ENV']}")
print(f"The secret key is: {service1.config['SECRET_KEY']}")

# Import Routes --------------------------------------------------------

bootstrap = Bootstrap(service1)

import service1_routes