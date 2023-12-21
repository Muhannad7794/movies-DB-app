import pytest
from movies.models import Directors
from movies.serializers import DirectorsSerializer

@pytest.mark.django_db
def test_directors_serializer():
    director_data = {
        "director_name": "Christopher Nolan",
        "nationality": "British-American",
        "director_date_of_birth": "1970-07-30",
        "director_best_movies": "Inception, Interstellar, The Dark Knight",
        "awards": "Academy Award"
    }
    director = Directors.objects.create(**director_data)
    serializer = DirectorsSerializer(director)

    # Update the expected data to include the 'id' field
    expected_data = dict(director_data)
    expected_data["id"] = director.id

    assert serializer.data == expected_data
