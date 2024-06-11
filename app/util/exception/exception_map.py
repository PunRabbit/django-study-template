from typing import Dict, Tuple, Callable, Type

from app.util.exception import exception_class
from app.util.exception import exception_action


EXCEPTION_MAP: Dict[Type[Exception], Tuple[int, str, Callable]] = {
    exception_class.CustomSampleException: (500, "BaseException", exception_action.error_notification)
}
