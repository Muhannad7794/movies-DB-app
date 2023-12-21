import pytest
from movies.models import MovieInfo, Directors, Studios


@pytest.mark.django_db
def test_movieinfo_str():
    director = Directors.objects.create(
        director_name="Christopher Nolan",
        director_date_of_birth="1970-07-30",
    )

    studio = Studios.objects.create(name="Warner Bros.", founded=1923)

    movie = MovieInfo.objects.create(
        title="Inception",
        genre="Science Fiction",
        release_year=2010,
        director=director,
        credits_score=8.8,
        studio=studio,
    )

    assert str(movie) == "Inception"


@pytest.mark.django_db
def test_directors_str():
    director = Directors.objects.create(
        director_name="Christopher Nolan",
        nationality="British",
        director_date_of_birth="1970-07-30",
        awards="Oscar",
    )

    assert str(director) == "Christopher Nolan"


@pytest.mark.django_db
def test_studios_str():
    studio = Studios.objects.create(
        name="Warner Bros.", founded=1923, location="Burbank, California, United States"
    )

    assert str(studio) == "Warner Bros."
