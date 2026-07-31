"""
WSGI config for artclub project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application


sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artclub.settings')

application = get_wsgi_application()
