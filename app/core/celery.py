import os
from celery import Celery

from app.core.constant import CONSTANT


os.environ.setdefault("DJANGO_SETTINGS_MODULE", CONSTANT.SETTING_FILE_PATH)

celery_app: Celery = Celery(CONSTANT.CELERY_CONFIG.CELERY_NAME)
celery_app.config_from_object(
    "django.conf:settings", namespace="CELERY"
)
celery_app.autodiscover_tasks()
