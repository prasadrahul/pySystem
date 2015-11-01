pySystem
========
System administration using python web framework


## Basic web Development setup using python and Django
---

**With Windows OS:**

**1. Install python 2.7**

Download Python Installer from [https://www.python.org/downloads/] (https://www.python.org/downloads/)

**2. Install PIP**

`$ easy_install pip`

**3. Install and check Django setup**

`$ pip install django==1.7`

`$ python -c "import django; print(django.get_version())"`

## Django Project Example
---

**Create New Project i.e. pySystem**

`$ django-admin startproject pySystem`

This will create project directory as shown


>pySystem/

>  |-  manage.py
>
>  |-  pySystem/
>
>      |-  __init__.py
>
>      |- settings.py
>
>      |- urls.py
>
>      |- wsgi.py


* The outer pySystem/ root directory is just a container for your project.
Its name doesn’t matter to Django; you can rename it to anything you like.

* manage.py:
A command-line utility that lets you interact with this Django project in various ways.
You can read all the details about manage.py in django-admin.py and manage.py.

* The inner pySystem/ directory is the actual Python package for your project.
Its name is the Python package name you’ll need to use to import anything inside it (e.g. pySystem.urls).

* pySystem/__init__.py:
An empty file that tells Python that this directory should be considered a Python package.
(Read more about packages in the official Python docs if you’re a Python beginner.)

* pySystem/settings.py:
Settings/configuration for this Django project. Django settings will tell you all about how settings work.

* pySystem/urls.py:
The URL declarations for this Django project; a “table of contents” of your Django-powered site.
You can read more about URLs in URL dispatcher.

* pySystem/wsgi.py:
An entry-point for WSGI-compatible web servers to serve your project.
See How to deploy with WSGI for more details.

**Install a MySQL database adapter for Python**

`$ pip install mysqlclient `

**Modify Database setting as per requirement**

vi pySystem\settings.py

>
>DATABASES =
> {

>    'default': {
>
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql', #works with windows
        #'ENGINE': 'mysql.connector.django', #work with linux
        'NAME': 'py_system',
        'USER': 'root',
        'PASSWORD': 'mysqlpassword',
        'HOST': 'localhost',
    }
}

`$ python manage.py migrate  #to install DB for pre installed apps`

---

>mysql> use py_system;

>Database changed

>mysql> show tables;

>+----------------------------+

>| Tables_in_py_system        |

>+----------------------------+

>| auth_group                 |

>| auth_group_permissions     |

>| auth_permission            |

>| auth_user                  |

>| auth_user_groups           |

>| auth_user_user_permissions |

>| django_admin_log           |

>| django_content_type        |

>| django_migrations          |

>| django_session             |

>+----------------------------+

>10 rows in set (0.00 sec)

**Create New App**

`$ python manage.py startapp sysadmin`


**Run Django WEB Server**

`$ python manage.py runserver`

---

Performing system checks...


System check identified no issues (0 silenced).


November 01, 2015 - 09:05:29


Django version 1.7, using settings 'pySystem.settings'


Starting development server at http://127.0.0.1:8000/


Quit the server with CTRL-BREAK.}