from rest_framework.routers import DefaultRouter

from app.apps.user import view


user_router: DefaultRouter = DefaultRouter()
user_router.register(prefix=r"user", viewset=view.UserViewSet)
