from django.urls import resolve, reverse
from movies.views import (
    MovieInfoViewSet,
    DirectorsViewSet,
    StudiosViewSet,
    PostersViewSet,
    StudiosImagesViewSet,
    DirectorsImagesViewSet,
    movie_recommendations,
)


def test_movies_url_resolves():
    url = reverse("movieinfo-list")
    assert resolve(url).func.cls == MovieInfoViewSet


def test_directors_url_resolves():
    url = reverse("directors-list")
    assert resolve(url).func.cls == DirectorsViewSet


def test_studios_url_resolves():
    url = reverse("studios-list")
    assert resolve(url).func.cls == StudiosViewSet


def test_posters_url_resolves():
    url = reverse("posters-list")
    assert resolve(url).func.cls == PostersViewSet


def test_studios_images_url_resolves():
    url = reverse("studiosimages-list")
    assert resolve(url).func.cls == StudiosImagesViewSet


def test_directors_images_url_resolves():
    url = reverse("directorsimages-list")
    assert resolve(url).func.cls == DirectorsImagesViewSet


def test_movie_recommendations_url():
    # Example movie_id for test
    movie_id = 1
    url = reverse("movie-recommendations", kwargs={"movie_id": movie_id})
    # Use resolve() to get the view function associated with the URL
    resolved_view_func = resolve(url).func

    # Assert that the resolved view function is movie_recommendations
    assert resolved_view_func == movie_recommendations
