# movies/views.py
from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import MovieInfo, Directors, Studios
from .serializers import (
    MovieInfoSerializer,
    DirectorsSerializer,
    StudiosSerializer,
    
)


class MovieInfoViewSet(viewsets.ModelViewSet):
    queryset = MovieInfo.objects.all()
    serializer_class = MovieInfoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "title",
        "release_year",
        "genre",
        "director__director_name",
        "credits_score",
        "studio__name",
    ]
    ordering_fields = ["title", "release_year", "credits_score"]


class DirectorsViewSet(viewsets.ModelViewSet):
    queryset = Directors.objects.all()
    serializer_class = DirectorsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["director_name", "nationality", "awards"]
    ordering_fields = ["director_name", "director_date_of_birth"]


class StudiosViewSet(viewsets.ModelViewSet):
    queryset = Studios.objects.all()
    serializer_class = StudiosSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name", "founded"]
