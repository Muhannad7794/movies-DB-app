import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
def test_movie_recommendations_movie_not_found():
    # Initialize the test client
    client = APIClient()

    # Use a movie ID that does not exist in the database
    non_existent_movie_id = 9999

    # Make a GET request to the movie_recommendations view
    path = reverse("movie-recommendations", kwargs={"movie_id": non_existent_movie_id})
    response = client.get(path)

    # Assert that the response status code is 404 (Not Found)
    assert response.status_code == 404

    # Assert that the error message is as expected
    assert response.json() == {"error": "Movie not found"}
