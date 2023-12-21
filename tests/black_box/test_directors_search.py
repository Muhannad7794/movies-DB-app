import pytest
from rest_framework.test import APIClient
from movies.models import Directors


@pytest.mark.django_db
class TestDirectorsViewSet:
    @pytest.fixture(autouse=True)
    def setup_class(self, db):
        self.client = APIClient()
        Directors.objects.create(
            director_name="Steven Spielberg",
            nationality="American",
            director_date_of_birth="1946-12-18",
            director_best_movies="Jaws, Schindler's List, Jurassic Park",
            awards="Academy Award, Golden Globe",
        )
        Directors.objects.create(
            director_name="Quentin Tarantino",
            nationality="American",
            director_date_of_birth="1963-03-27",
            director_best_movies="Pulp Fiction, Django Unchained, Kill Bill",
            awards="Academy Award, Golden Globe Award",
        )

    def test_search_by_name(self):
        response = self.client.get("/movies/directors/", {"search": "Steven Spielberg"})
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["director_name"] == "Steven Spielberg"

    def test_search_by_nationality(self):
        response = self.client.get("/movies/directors/", {"search": "American"})
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_search_by_awards(self):
        response = self.client.get("/movies/directors/", {"search": "Academy Award"})
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_invalid_search_query(self):
        response = self.client.get("/movies/directors/", {"search": "Unknown"})
        assert response.status_code == 200
        assert len(response.data) == 0
