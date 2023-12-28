import responses
from movies.services.recommend import TMDBService
from django.conf import settings


@responses.activate
def test_get_similar_movies_server_error():
    # Create an instance of TMDBService
    tmdb_service = TMDBService()

    # Mock URL for similar movies
    movie_id = 123
    mock_url = f"{tmdb_service.base_url}/movie/{movie_id}/similar"

    # Add mock response for 500 Server Error
    responses.add(
        responses.GET,
        mock_url,
        json={"status_message": "Internal Server Error"},
        status=500,
    )

    # Call the get_similar_movies method
    result = tmdb_service.get_similar_movies(movie_id)

    # Assert the error message is returned
    assert result == {"error": "TMDB API is facing problems."}
