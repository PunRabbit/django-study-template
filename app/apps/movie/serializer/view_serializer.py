from rest_framework import serializers

from app.apps.movie.serializer.model_serializer import DirectorSerializer


class MovieInfoSerializer(serializers.Serializer):
    movie_info: serializers.ModelSerializer = DirectorSerializer()
    is_valid = serializers.BooleanField()


