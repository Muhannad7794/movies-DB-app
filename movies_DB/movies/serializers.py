# movies/serializers.py
from rest_framework import serializers
from .models import MovieInfo, Directors, Studios


class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directors
        fields = "__all__"


class StudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studios
        fields = "__all__"


class MovieInfoSerializer(serializers.ModelSerializer):
    director = DirectorsSerializer(read_only=True)
    studio = StudiosSerializer(read_only=True)

    class Meta:
        model = MovieInfo
        fields = "__all__"
