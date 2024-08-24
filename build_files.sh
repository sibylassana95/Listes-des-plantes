#!/bin/bash

echo "BUILD START"

# create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv venv

# activate the virtual environment
source venv/bin/activate

# upgrade pip and setuptools
pip install --upgrade pip setuptools

# install all deps in the venv
pip install -r requirements.txt

# collect static files
python manage.py collectstatic --noinput

echo "BUILD END"
