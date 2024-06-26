"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``domain``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from app.setting.constant import CONSTANT

os.environ.setdefault("DJANGO_SETTINGS_MODULE", CONSTANT.SETTING_FILE_PATH)

application = get_wsgi_application()
