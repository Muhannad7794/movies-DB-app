import pytest
from movies.models import MovieInfo, Directors, Studios
from movies.serializers import MovieInfoSerializer, DirectorsSerializer, StudiosSerializer

@pytest.mark.django_db
def test_movie_info_serializer():
    director = Directors.objects.create(
        director_name="Christopher Nolan",
        nationality="British-American",
        director_date_of_birth="1970-07-30",
        director_best_movies="Inception, Interstellar, The Dark Knight",
        awards="Academy Award"
    )
    studio = Studios.objects.create(
        name="Warner Bros.",
        founded=1923,
        location="Burbank, California, United States"
    )
    movie_info = MovieInfo.objects.create(
        title="Inception",
        genre="Science Fiction",
        release_year=2010,
        director=director,
        credits_score=8.8,
        studio=studio
    )
    serializer = MovieInfoSerializer(movie_info)

    # Update the expected data to include the 'id' field and serialized director and studio data
    expected_data = {
        "id": movie_info.id,
        "title": "Inception",
        "genre": "Science Fiction",
        "release_year": 2010,
        "credits_score": 8.8,
        "director": DirectorsSerializer(director).data,
        "studio": StudiosSerializer(studio).data
    }

    assert serializer.data == expected_data
