import responses
from movies.services.recommend import TMDBService
from django.conf import settings


@responses.activate
def test_get_similar_movies_rate_limit_exceeded():
    # Create an instance of TMDBService
    tmdb_service = TMDBService()

    # Mock URL for similar movies
    movie_id = 123  # Example movie ID
    mock_url = f"{tmdb_service.base_url}/movie/{movie_id}/similar"

    # Add mock response for 429 Rate Limit Exceeded
    responses.add(
        responses.GET,
        mock_url,
        json={"status_message": "Rate limit exceeded"},
        status=429,
    )

    # Call the get_similar_movies method
    result = tmdb_service.get_similar_movies(movie_id)

    # Assert the error message for rate limit exceeded is returned
    assert result == {"error": "Rate limit exceeded."}
