import pytest
from django.utils import timezone
from movies.models import Directors

@pytest.mark.django_db
def test_director_creation():
    director = Directors.objects.create(
        director_name="Christopher Nolan",
        nationality="British-American",
        director_date_of_birth=timezone.datetime(1970, 7, 30).date(),
        director_best_movies="Inception, Interstellar, The Dark Knight",
        awards="Academy Award"
    )
    assert director.director_name == "Christopher Nolan"
    assert Directors.objects.count() == 1
