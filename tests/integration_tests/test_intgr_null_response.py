import responses
from movies.services.recommend import TMDBService
from django.conf import settings


@responses.activate
def test_search_movie_no_results():
    # Create an instance of TMDBService
    tmdb_service = TMDBService()

    # Mock URL
    mock_url = f"{tmdb_service.base_url}/search/movie"

    # Mock response for no results
    responses.add(
        responses.GET,
        mock_url,
        json={"results": []},
        status=200,
    )

    # Call the search_movie method
    result = tmdb_service.search_movie("Nonexistent Movie Title")

    # Assert the result is None
    assert result is None
