import pytest
from rest_framework.test import APIClient
from movies.models import Directors

@pytest.mark.django_db
def test_directors_list():
    client = APIClient()
    Directors.objects.create(
        director_name="Director Name",
        nationality="Nationality",
        director_date_of_birth="1970-01-01",  # Provide a valid date here
        director_best_movies="Best Movies",
        awards="Awards",
    )

    response = client.get("/movies/directors/")
    assert response.status_code == 200
    assert response.data[0]["director_name"] == "Director Name"
    assert response.data[0]["nationality"] == "Nationality"
    assert response.data[0]["director_date_of_birth"] == "1970-01-01"
    assert response.data[0]["director_best_movies"] == "Best Movies"
    assert response.data[0]["awards"] == "Awards"
