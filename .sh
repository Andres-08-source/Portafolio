#!/bin/bash
python manage.py migrate
gunicorn Portafolio.wsgi
