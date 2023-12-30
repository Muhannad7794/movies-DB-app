import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from movies.models import MovieInfo, Directors, Studios, Posters

from django.test import RequestFactory
from django.core.files.base import ContentFile


@pytest.mark.django_db
def test_posters_model():
    # Set up movie, director, and studio
    director = Directors.objects.create(
        director_name="Christopher Nolan",
        nationality="British",
        director_date_of_birth="1970-07-30",
        director_best_movies="Inception, Interstellar, The Dark Knight",
        awards="Academy Award",
    )
    studio = Studios.objects.create(
        name="Warner Bros.", founded=1923, location="Burbank, California, United States"
    )
    movie_info = MovieInfo.objects.create(
        title="Inception",
        genre="Science Fiction",
        release_year=2010,
        director=director,
        credits_score=8.8,
        studio=studio,
    )

    # Create a mock poster file
    poster_content = b"file_content"
    poster_file = SimpleUploadedFile(
        "poster.jpg", poster_content, content_type="image/jpeg"
    )
    # create a poster instance
    poster = Posters.objects.create(movie=movie_info, poster=poster_file)
    # assert that the poster is created and the movie has a poster
    assert Posters.objects.count() == 1
    # assert the values of the poster
    assert poster.movie == movie_info

    # Read the content of the saved poster file for comparison
    saved_poster_content = poster.poster.read()

    # Assert the content of the saved file matches the original content
    assert saved_poster_content == poster_content

    # Assert that the poster object has a file associated with it
    assert poster.poster is not None
