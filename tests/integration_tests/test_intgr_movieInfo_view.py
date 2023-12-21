import pytest
from rest_framework.test import APIClient
from movies.models import MovieInfo, Directors, Studios


@pytest.mark.django_db
def test_movie_info_list():
    client = APIClient()
    director = Directors.objects.create(
        director_name="Director Name",
        nationality="Nationality",
        director_date_of_birth="1970-01-01",
        director_best_movies="Best Movies",
        awards="Awards",
    )
    studio = Studios.objects.create(name="Name", founded=2020, location="Location")
    MovieInfo.objects.create(
        title="Test Movie",
        director=director,
        studio=studio,
        genre="Genre",
        release_year=2020,
        credits_score=8.8,
    )

    response = client.get("/movies/movies/")
    assert response.status_code == 200
    assert response.data[0]["title"] == "Test Movie"
    assert response.data[0]["director"]["director_name"] == "Director Name"
    assert response.data[0]["studio"]["name"] == "Name"
    assert response.data[0]["genre"] == "Genre"
    assert response.data[0]["release_year"] == 2020
    assert response.data[0]["credits_score"] == 8.8
