from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Constant:
    SETTING_FILE_PATH: str = "app.setting.settings"
    SETTING_MAIN_URL_FILE_PATH: str = "app.setting.urls"
    TIME_ZONE: str = "Asia/Seoul"
    USE_TZ: bool = False

    @dataclass(frozen=True)
    class CeleryConfig:
        CELERY_NAME: str = "toss-celery"

        CELERY_BROKER_URL: str = "redis://toss-redis:6379/0"
        CELERY_RESULT_BACKEND: str = "django-db"
        CELERY_ACCEPT_CONTENT: List[str] = field(default_factory=lambda: ["json"])
        CELERY_TASK_SERIALIZER: str = "json"
        CELERY_RESULT_SERIALIZER: str = "json"
        CELERY_TIMEZONE: str = "Asia/Seoul"

    @dataclass(frozen=True)
    class CustomDBConfig:
        MARIADB_CONFIG: dict = field(
            default_factory=lambda: {
                "ENGINE": "django.db.backends.mysql",
                "NAME": "toss",
                "USER": "root",
                "PASSWORD": "toss",
                "HOST": "toss-mariadb",
                "PORT": "3306",
            }
        )

    CELERY_CONFIG: CeleryConfig = CeleryConfig()
    DATABASE_CONFIG: CustomDBConfig = CustomDBConfig()


CONSTANT: Constant = Constant()
