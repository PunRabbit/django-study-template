from rest_framework import serializers

from app.apps.movie.models import Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name']

