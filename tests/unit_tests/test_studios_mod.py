import pytest
from movies.models import Studios


@pytest.mark.django_db
def test_studio_creation():
    studio = Studios.objects.create(
        name="Warner Bros.", founded=1923, location="Burbank, California, United States"
    )
    assert studio.name == "Warner Bros."
    assert studio.founded == 1923
    assert studio.location == "Burbank, California, United States"
    assert Studios.objects.count() == 1
