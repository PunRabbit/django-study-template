from rest_framework.routers import DefaultRouter

from app.apps.user.view import UserViewSet


user_router: DefaultRouter = DefaultRouter()
user_router.register(prefix=r"user", viewset=UserViewSet)
