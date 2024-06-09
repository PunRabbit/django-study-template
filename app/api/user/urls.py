from rest_framework.routers import DefaultRouter

from app.api.user.view import UserListViewSet


user_router: DefaultRouter = DefaultRouter()
user_router.register(r'user', UserListViewSet)
