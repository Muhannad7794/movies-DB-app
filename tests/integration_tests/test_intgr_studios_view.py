import pytest
from rest_framework.test import APIClient
from movies.models import Studios


@pytest.mark.django_db
def test_studios_list():
    client = APIClient()
    Studios.objects.create(name="Name", founded=2020, location="Location")

    response = client.get(
        "/movies/studios/"
    )  # Update URL based on your project's routing
    assert response.status_code == 200
    assert response.data[0]["name"] == "Name"
    assert response.data[0]["founded"] == 2020
    assert response.data[0]["location"] == "Location"
