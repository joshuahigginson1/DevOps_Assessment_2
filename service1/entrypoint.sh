echo "Creating Database... \n \n"
exec python3 create.py
echo "Created Database?? \n \n "
exec gunicorn -c service1_gunicorn_config.py service1_wsgi:service1