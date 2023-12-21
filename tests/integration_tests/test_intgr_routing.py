from django.urls import resolve, reverse
from movies.views import MovieInfoViewSet, DirectorsViewSet, StudiosViewSet


def test_movies_url_resolves():
    url = reverse("movieinfo-list")
    assert resolve(url).func.cls == MovieInfoViewSet


def test_directors_url_resolves():
    url = reverse("directors-list")
    assert resolve(url).func.cls == DirectorsViewSet


def test_studios_url_resolves():
    url = reverse("studios-list")
    assert resolve(url).func.cls == StudiosViewSet
