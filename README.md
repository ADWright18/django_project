# Author: Adomous Wright
# Date: 12/25/17

This is a repository to test and learn Django and create a website. Feel free to give me feedback!

# How to start a django project
django-admin startproject (project_name)

# How to start dev server
python manage.py runserver (port_number)

# How to create a new app
python manage.py startapp (app_name)

# How to add a new app
INSTALLED_APPS = [
    '(app_name).apps.(App_name)Config',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# How to migrate database
python manage.py migrate
