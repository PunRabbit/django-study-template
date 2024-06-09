import os
from celery import Celery
from celery.schedules import crontab

from app.core.constant import CONSTANT


os.environ.setdefault("DJANGO_SETTINGS_MODULE", CONSTANT.SETTING_FILE_PATH)

celery_app: Celery = Celery(CONSTANT.CELERY_CONFIG.CELERY_NAME)
celery_app.config_from_object(
    "django.conf:settings", namespace="CELERY"
)
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'myapp.tasks.add',
        # 'schedule': 30.0,
        'schedule': crontab(hour='7', minute='30', day_of_week='1'), # 매주 월요일 7시 30분에 실행
        'args': (16, 16),
    },
}
