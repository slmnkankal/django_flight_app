# DJANGO SETTINGS

Seperating settings.py additional notes:

## DEBUG

DEBUG needs to be True on dev, and False on prod. So, we can also seperate DEBUG.

- Open dev.py and add:
```py
DEBUG = True
```

- Open prod.py and add:
```py
DEBUG = False
```

- Remove DEBUG from .env file and base.py.

## ALLOWED_HOSTS

ALLOWED_HOSTS is a list of strings representing the host/domain names 
that this Django site can serve.

When DEBUG is True and ALLOWED_HOSTS is empty, the host is validated 
against ['.localhost', '127.0.0.1', '[::1]'].

When DEBUG is False, you need to add a hostname here (e.g. 'www.example.com' 
or '\*'). A value of * which will match anything. 

- Open dev.py and add:
```py
ALLOWED_HOSTS = []
```

- Open prod.py and add:
```py
# Until we deploy our project, we do not know the hosting server,
# so, keep it allowing all for now.
# Change this field when you deploy your project.
ALLOWED_HOSTS = ['*']
```

- Remove ALLOWED_HOSTS from base.py.

## LOGGING

Logs are important especially on production environment. 
For development, you see DEBUG info immediately from console 
and from browser if there is any error on your page. So, 
keeping logger for only prod may be prefferred.

- Cut LOGGING from base.py and add it to the prod.py.

Happy Coding!!!