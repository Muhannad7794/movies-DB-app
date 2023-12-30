import pytest
from django.utils import timezone
from movies.models import Directors


@pytest.mark.django_db
def test_director_creation():
    director = Directors.objects.create(
        director_name="Christopher Nolan",
        nationality="British",
        director_date_of_birth=timezone.datetime(1970, 7, 30).date(),
        director_best_movies="Inception, Interstellar, The Dark Knight",
        awards="Academy Award",
    )
    assert director.director_name == "Christopher Nolan"
    assert director.nationality == "British"
    assert director.director_date_of_birth == timezone.datetime(1970, 7, 30).date()
    assert director.director_best_movies == "Inception, Interstellar, The Dark Knight"
    assert director.awards == "Academy Award"
    assert Directors.objects.count() == 1
