import pytest
from movies.models import (
    MovieInfo,
    Directors,
    Studios,
    Posters,
    DirectorsImages,
    StudiosImages,
)


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


@pytest.mark.django_db
def test_posters_str():
    # First, create a Director and Studio instance as they are required for MovieInfo
    director = Directors.objects.create(
        director_name="Christopher Nolan",
        nationality="British",
        director_date_of_birth="1970-07-30",
        awards="Oscar",
    )
    studio = Studios.objects.create(
        name="Warner Bros.", founded=1923, location="Burbank, California, United States"
    )

    # Now create a MovieInfo instance
    movie = MovieInfo.objects.create(
        title="Inception",
        genre="Science Fiction",
        release_year=2010,
        director=director,
        credits_score=8.8,
        studio=studio,
    )

    # Create the Posters instance with the movie_info instance
    poster = Posters.objects.create(movie=movie, poster=None)

    # Your assertion remains the same
    assert str(poster) == movie.title


@pytest.mark.django_db
def test_directors_pictures_str():
    # First, create a Director instance
    director = Directors.objects.create(
        director_name="Christopher Nolan",
        nationality="British",
        director_date_of_birth="1970-07-30",
        awards="Oscar",
    )

    # Now create a DirectorsImages instance
    director_image = DirectorsImages.objects.create(director=director, picture=None)

    # assert that the __str__ method returns the director name
    assert str(director_image) == director.director_name


@pytest.mark.django_db
def test_studios_pictures_str():
    # First, create a Studio instance
    studio = Studios.objects.create(
        name="Warner Bros.",
        founded=1923,
        location="Burbank, California, United States",
    )

    # Now create a StudiosImages instance
    studio_image = StudiosImages.objects.create(studio=studio, picture=None)

    # assert that the __str__ method returns the studio name
    assert str(studio_image) == studio.name
