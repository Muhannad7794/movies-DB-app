# movies/serializers.py
from rest_framework import serializers
from .models import MovieInfo, Directors, Studios, Posters, DirectorsImages


class DirectorsSerializer(serializers.ModelSerializer):
    picture_url = serializers.SerializerMethodField()

    class Meta:
        model = Directors
        fields = "__all__"

    def get_picture_url(self, obj):
        picture = DirectorsImages.objects.filter(director=obj).first()
        if picture and picture.picture:
            return self.context["request"].build_absolute_uri(picture.picture.url)
        return None


class StudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studios
        fields = "__all__"


class MovieInfoSerializer(serializers.ModelSerializer):
    director = DirectorsSerializer(read_only=True)
    studio = StudiosSerializer(read_only=True)
    poster_url = serializers.SerializerMethodField()

    class Meta:
        model = MovieInfo
        fields = "__all__"

    def get_poster_url(self, obj):
        poster = Posters.objects.filter(movie=obj).first()
        if poster and poster.poster:
            return self.context["request"].build_absolute_uri(poster.poster.url)
        return None  # Or a default image URL


class PostersSerializer(serializers.ModelSerializer):
    poster = serializers.ImageField(use_url=True)

    class Meta:
        model = Posters
        fields = "__all__"


class DirectorsImagesSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(use_url=True)

    class Meta:
        model = DirectorsImages
        fields = "__all__"
