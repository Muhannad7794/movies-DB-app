# movies/serializers.py
from rest_framework import serializers
from .models import MovieInfo, Directors, Studios

class MovieInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = '__all__'

class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directors
        fields = '__all__'

class StudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studios
        fields = '__all__'
