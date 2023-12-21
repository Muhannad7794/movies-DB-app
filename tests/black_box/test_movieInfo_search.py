import pytest
from rest_framework.test import APIClient
from movies.models import MovieInfo, Directors, Studios


@pytest.mark.django_db
class TestMovieInfoViewSet:
    @pytest.fixture(autouse=True)
    def setup_class(self, db):
        self.client = APIClient()

        director = Directors.objects.create(
            director_name="Christopher Nolan",
            nationality="British",
            awards="Oscar",
            director_date_of_birth="1970-07-30",
        )
        studio = Studios.objects.create(
            name="Warner Bros.",
            founded=1923,
            location="Burbank, California, United States",
        )
        MovieInfo.objects.create(
            title="Inception",
            genre="Science Fiction",
            release_year=2010,
            director=director,
            credits_score=8.8,
            studio=studio,
        )
        MovieInfo.objects.create(
            title="Interstellar",
            genre="Adventure, Drama, Science Fiction",
            release_year=2014,
            director=director,
            credits_score=8.6,
            studio=studio,
        )

    def test_search_by_title(self):
        response = self.client.get("/movies/movies/", {"search": "Inception"})
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["title"] == "Inception"

    def test_search_by_genre(self):
        response = self.client.get("/movies/movies/", {"search": "Science Fiction"})
        assert response.status_code == 200
        assert len(response.data) == 2  # Both movies fall under this genre

    def test_search_by_director(self):
        response = self.client.get("/movies/movies/", {"search": "Christopher Nolan"})
        assert response.status_code == 200
        assert len(response.data) == 2  # Both movies were directed by Christopher Nolan

    def test_search_by_studio(self):
        response = self.client.get("/movies/movies/", {"search": "Warner Bros."})
        assert response.status_code == 200
        assert len(response.data) == 2  # Both movies were produced by Warner Bros.

    def test_search_by_release_year(self):
        response = self.client.get("/movies/movies/", {"search": "2010"})
        assert response.status_code == 200
        assert len(response.data) == 1

    def test_search_by_credits_score(self):
        response = self.client.get("/movies/movies/", {"search": "8.8"})
        assert response.status_code == 200
        assert len(response.data) == 1

    def test_search_by_two_fields(self):
        response = self.client.get(
            "/movies/movies/", {"search": "Christopher Nolan 2010"}
        )
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["title"] == "Inception"

    def test_search_by_multiple_fields(self):
        response = self.client.get(
            "/movies/movies/", {"search": "Christopher Nolan 2014 Science Fiction"}
        )
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["title"] == "Interstellar"

    def test_invalid_search_query(self):
        response = self.client.get("/movies/movies/", {"search": "123"})
        assert response.status_code == 200
        assert len(response.data) == 0
