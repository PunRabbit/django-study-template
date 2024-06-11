# from rest_framework.views import exception_handler
# from rest_framework.response import Response
# from rest_framework import status
#
#
# def global_exception_handler(exc, context):
#     response = exception_handler(exc, context)
#     for exception_type, (status_code, name) in EXCEPTION_MAP.items():
#         if isinstance(exc, exception_type):
#             return Response(
#                 status_code=status_code,
#                 content=ErrorResponse(info=name, message=exc.__str__()).dict(),
#             )
#
#     return response


