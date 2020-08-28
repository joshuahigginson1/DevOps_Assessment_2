printenv
exec python3 create.py
exec gunicorn -c service1_gunicorn_config.py service1_wsgi:service1