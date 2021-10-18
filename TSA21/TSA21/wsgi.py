"""
WSGI config for TSA21 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/Documents/DjangoTSA21/TSA21')
sys.path.append('/Documents/DjangoTSA21/TSA21/default')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TSA21.settings")

application = get_wsgi_application()
