import responses
from movies.services.recommend import TMDBService
from django.conf import settings

@responses.activate
def test_get_similar_movies_nonexistent_movie():
    # Create an instance of TMDBService
    tmdb_service = TMDBService()

    # Mock URL for similar movies of a non-existent movie
    nonexistent_movie_id = 9999  # Example non-existent movie ID
    mock_url = f"{tmdb_service.base_url}/movie/{nonexistent_movie_id}/similar"

    # Add mock response for 404 Not Found
    responses.add(
        responses.GET,
        mock_url,
        json={"status_message": "Movie not found."},
        status=404,
    )

    # Call the get_similar_movies method with the non-existent movie ID
    result = tmdb_service.get_similar_movies(nonexistent_movie_id)

    # Assert the error message is returned
    assert result == {"error": "Movie not found."}
