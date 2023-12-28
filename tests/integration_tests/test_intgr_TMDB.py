import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from movies.models import MovieInfo, Directors, Studios


@pytest.mark.django_db
def test_movie_recommendations_integration_with_real_api():
    # Set up the movie object in the test database
    director = Directors.objects.create(
        director_name="Christopher Nolan",
        nationality="British-American",
        director_date_of_birth="1970-07-30",
        director_best_movies="Inception, The Dark Knight",
        awards="Academy Award",
    )
    studio = Studios.objects.create(
        name="Warner Bros", founded=1923, location="Burbank"
    )
    movie = MovieInfo.objects.create(
        title="Inception",
        director=director,
        studio=studio,
        genre="Sci-Fi",
        release_year=2010,
        credits_score=8.8,
    )

    # Initialize the test client
    client = APIClient()

    # Fetch the recommendations using the real API
    path = reverse("movie-recommendations", kwargs={"movie_id": movie.id})
    response = client.get(path)

    # Check the status code
    assert response.status_code == 200

    # Further assertions can be made based on the actual content of the response
    # For example, check if the 'results' key is in the response
    assert "results" in response.json()

    # And if you expect at least one recommendation:
    assert len(response.json()["results"]) == 6
