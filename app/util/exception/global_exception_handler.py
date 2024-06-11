from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

from app.util.exception.exception_map import EXCEPTION_MAP


def global_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        for exception_type, (status_code, msg, action) in EXCEPTION_MAP.items():
            if isinstance(exc, exception_type):
                action()
                return Response({"message": msg}, status=status_code)

    return response
