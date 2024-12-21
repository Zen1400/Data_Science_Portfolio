"""
WSGI config for django_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# I believe this was behind the modeul 'app' not found. Including it in the Dockerfile made it work
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_api.settings')

application = get_wsgi_application()
