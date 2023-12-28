import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from movies.models import MovieInfo, Directors, Studios, Posters
from movies.serializers import (
    MovieInfoSerializer,
    DirectorsSerializer,
    StudiosSerializer,
)
from django.test import RequestFactory


@pytest.mark.django_db
def test_movie_info_serializer_with_poster():
    # Set up movie, director, and studio
    director = Directors.objects.create(
        director_name="Christopher Nolan",
        nationality="British-American",
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
    poster_file = SimpleUploadedFile(
        "poster.jpg", b"file_content", content_type="image/jpeg"
    )
    poster = Posters.objects.create(movie=movie_info, poster=poster_file)

    # Create a request object to pass as context to the serializer
    request = RequestFactory().get("/")
    serializer_context = {"request": request}

    # Create the serializer with the movie_info instance and context
    serializer = MovieInfoSerializer(movie_info, context=serializer_context)

    # Construct the expected data
    expected_data = {
        "id": movie_info.id,
        "title": "Inception",
        "genre": "Science Fiction",
        "release_year": 2010,
        "credits_score": 8.8,
        "director": DirectorsSerializer(director).data,
        "studio": StudiosSerializer(studio).data,
        "poster_url": request.build_absolute_uri(poster.poster.url),
    }

    assert serializer.data == expected_data
