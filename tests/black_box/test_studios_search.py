import pytest
from rest_framework.test import APIClient
from movies.models import MovieInfo, Directors, Studios


@pytest.mark.django_db
class TestStudiosViewSet:
    @pytest.fixture(autouse=True)
    def setup_class(self, db):
        self.client = APIClient()

        Studios.objects.create(
            name="Pixar", founded=1986, 
            location="Emeryville, California, United States"
        )
        Studios.objects.create(
            name="Studio Ghibli", founded=1985, 
            location="Koganei, Tokyo, Japan"
        )

    def test_search_by_name(self):
        response = self.client.get("/movies/studios/", {"search": "Pixar"})
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["name"] == "Pixar"

    def test_search_by_location(self):
        response = self.client.get("/movies/studios/", {"search": "Tokyo"})
        assert response.status_code == 200
        assert len(response.data) == 1 

    def test_invalid_search_query(self):
        response = self.client.get("/movies/studios/", {"search": "Nonexistent"})
        assert response.status_code == 200
        assert len(response.data) == 0

