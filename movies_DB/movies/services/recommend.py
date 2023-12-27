import requests
from django.conf import settings


class TMDBService:
    def __init__(self):
        self.api_key = settings.TMDB_API_KEY
        self.base_url = "https://api.themoviedb.org/3"

    def search_movie(self, title):
        search_url = (
            f"{self.base_url}/search/movie?api_key={self.api_key}&query={title}"
        )
        response = requests.get(search_url)
        if response.status_code == 200:
            results = response.json().get("results")
            if results:
                return results[0].get(
                    "id"
                )  # Assuming the first result is the correct movie
        return None

    def get_similar_movies(self, movie_id, number_of_recommendations=6):
        url = f"{self.base_url}/movie/{movie_id}/similar?api_key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            data["results"] = data["results"][:number_of_recommendations]
            return data

        else:
            return None
