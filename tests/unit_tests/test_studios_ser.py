import pytest
from movies.models import Studios
from movies.serializers import StudiosSerializer


@pytest.mark.django_db
def test_studios_serializer():
    studio_data = {
        "name": "Warner Bros.",
        "founded": 1923,
        "location": "Burbank, California, United States",
    }
    studio = Studios.objects.create(**studio_data)
    serializer = StudiosSerializer(studio)

    # Update the expected data to include the 'id' field
    expected_data = dict(studio_data)
    expected_data["id"] = studio.id

    # update to include the picture_url in the expected data
    expected_data["picture_url"] = None

    assert serializer.data == expected_data
