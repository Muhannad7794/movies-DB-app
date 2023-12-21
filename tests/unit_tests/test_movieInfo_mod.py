import pytest
from django.utils import timezone
from movies.models import MovieInfo, Directors, Studios

@pytest.mark.django_db
def test_movie_info_creation():
    director = Directors.objects.create(
        director_name="Christopher Nolan",
        nationality="British-American",
        director_date_of_birth=timezone.datetime(1970, 7, 30).date(),
        director_best_movies="Inception, Interstellar, The Dark Knight",
        awards="Academy Award"
    )
    studio = Studios.objects.create(
        name="Warner Bros.",
        founded=1923,
        location="Burbank, California, United States"
    )
    movie = MovieInfo.objects.create(
        title="Inception",
        genre="Science Fiction",
        release_year=2010,
        director=director,
        credits_score=8.8,
        studio=studio
    )
    assert movie.title == "Inception"
    assert MovieInfo.objects.count() == 1
