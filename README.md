# pySystem
System administration using python web framework


Basic web Development using Django
-------------------------------------
Windows-

1# Install python 2.7

Go to https://www.python.org/downloads/
and download link: https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi

2# Install PIP

$ easy_install pip

3# Install and check Django

$ pip install django==1.7

$ python -c "import django; print(django.get_version())"

---------------------------------

# Create New Project

$ django-admin startproject pySystem
========
pySystem/
  |
  |- manage.py
  |- pySystem/
       |-  __init__.py
       |- settings.py
       |- urls.py
       |- wsgi.py
=========
The outer pySystem/ root directory is just a container for your project.
Its name doesn’t matter to Django; you can rename it to anything you like.

manage.py:
A command-line utility that lets you interact with this Django project in various ways.
You can read all the details about manage.py in django-admin.py and manage.py.

The inner pySystem/ directory is the actual Python package for your project.
Its name is the Python package name you’ll need to use to import anything inside it (e.g. pySystem.urls).

pySystem/__init__.py:
An empty file that tells Python that this directory should be considered a Python package.
(Read more about packages in the official Python docs if you’re a Python beginner.)

pySystem/settings.py:
Settings/configuration for this Django project. Django settings will tell you all about how settings work.

pySystem/urls.py:
The URL declarations for this Django project; a “table of contents” of your Django-powered site.
You can read more about URLs in URL dispatcher.

pySystem/wsgi.py:
An entry-point for WSGI-compatible web servers to serve your project.
See How to deploy with WSGI for more details.
=========
$ pip install mysqlclient #install a MySQL database adapter for Python

#--------------------------------------

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',

        # 'ENGINE': 'mysql.connector.django', #work with linux
        'NAME': 'py_system',
        'USER': 'root',
        'PASSWORD': 'mysqlpassword',
        'HOST': 'localhost',
    }
}

#--------------------------------------------
$ python manage.py migrate  #to install DB for pre installed apps

$ python manage.py startapp sysadmin

$ python manage.py runserver