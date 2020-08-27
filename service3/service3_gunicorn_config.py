"""This file contains the config settings for Gunicorn."""

# Imports --------------------------------------------------------------

import multiprocessing

# Settings -------------------------------------------------------------

workers = multiprocessing.cpu_count() * 2 + 1  # Dynamically generates workers.
reload = True  # Restart workers when our code changes.

bind = "0.0.0.0:5003"

# logging
accesslog = '-'
errorlog = '-'
