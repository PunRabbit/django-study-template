from rest_framework.routers import DefaultRouter

from app.api.user.view import UserListViewSet


user_router: DefaultRouter = DefaultRouter()
user_router.register(prefix=r"user", viewset=UserListViewSet)
