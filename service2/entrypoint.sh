echo $(FLASK_ENV)

exec gunicorn -c service2_gunicorn_config.py service2_wsgi:service2