from rest_framework import viewsets, mixins
from rest_framework.views import APIView

from app.apps.user.models import User
from app.apps.user.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

