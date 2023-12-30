from django.conf import settings
from django.test import override_settings
import pytest
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from movies.models import MovieInfo, Directors, Studios, Posters


@override_settings(DEBUG=True)
@pytest.mark.django_db
def test_media_serving(client):
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

    # Make a request for the media file
    response = client.get(poster.poster.url)

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
