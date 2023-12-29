from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    MovieInfoViewSet,
    DirectorsViewSet,
    StudiosViewSet,
    PostersViewSet,
    DirectorsImagesViewSet,
    StudiosImagesViewSet,
    movie_recommendations,
)

router = DefaultRouter()
router.register(r"movies", MovieInfoViewSet)
router.register(r"directors", DirectorsViewSet)
router.register(r"studios", StudiosViewSet)
router.register(r"posters", PostersViewSet)
router.register(r"directors-images", DirectorsImagesViewSet)
router.register(r"studios-images", StudiosImagesViewSet)


urlpatterns = [
    path(
        "movies/<int:movie_id>/recommendations/",
        movie_recommendations,
        name="movie-recommendations",
    ),
] + router.urls
