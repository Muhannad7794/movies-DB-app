import responses
from movies.services.recommend import TMDBService
from django.conf import settings


@responses.activate
def test_get_similar_movies_unknown_error():
    # Create an instance of TMDBService
    tmdb_service = TMDBService()

    # Mock URL for similar movies
    movie_id = 123  # Example movie ID
    mock_url = f"{tmdb_service.base_url}/movie/{movie_id}/similar"

    # Add mock response for an unexpected status code, e.g., 418
    responses.add(
        responses.GET,
        mock_url,
        json={"status_message": "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"}, 
        status=418,  # unknown status code
    )

    # Call the get_similar_movies method
    result = tmdb_service.get_similar_movies(movie_id)

    # Assert the error message for an unknown error is returned
    assert result == {"error": "Unknown error."}
