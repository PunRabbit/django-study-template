from django.contrib.auth.models import Group, User
from rest_framework import serializers
from typing import List


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: User = User
        fields: List[str] = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Group = Group
        fields: List[str] = ['url', 'name']


