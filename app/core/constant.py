from dataclasses import dataclass


@dataclass(frozen=True)
class Constant:
    SETTING_FILE_PATH: str = 'app.core.settings'
    SETTING_MAIN_URL_FILE_PATH: str = 'app.api.urls'
    TIME_ZONE: str = 'Asia/Seoul'
    USE_TZ: bool = False


CONSTANT: Constant = Constant()
