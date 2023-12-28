import responses
from movies.services.recommend import TMDBService
from django.conf import settings


@responses.activate
def test_get_similar_movies_successful():
    # Create an instance of TMDBService
    tmdb_service = TMDBService()

    # Mock URL for similar movies
    movie_id = 123  # Example movie ID
    mock_url = f"{tmdb_service.base_url}/movie/{movie_id}/similar"

    # Mock response data
    mock_response_data = {
        "results": [
            {"id": 1, "title": "Similar Movie 1"},
            {"id": 2, "title": "Similar Movie 2"},
            {"id": 3, "title": "Similar Movie 3"},
            {"id": 4, "title": "Similar Movie 4"},
            {"id": 5, "title": "Similar Movie 5"},
            {"id": 6, "title": "Similar Movie 6"},
            # ...
        ]
    }

    # Number of recommendations expected
    number_of_recommendations = 6

    # Ensure the mock data has at least as many movies as the number of recommendations
    mock_response_data["results"] = mock_response_data["results"][
        :number_of_recommendations
    ]

    # Add mock response
    responses.add(
        responses.GET,
        mock_url,
        json=mock_response_data,
        status=200,
    )

    # Call the get_similar_movies method
    result = tmdb_service.get_similar_movies(movie_id, number_of_recommendations)

    # Assert the response structure and number of recommendations
    assert len(result["results"]) == number_of_recommendations
    for movie in result["results"]:
        assert "id" in movie and "title" in movie
