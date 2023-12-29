import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from movies.models import (
    MovieInfo,
    Directors,
    Studios,
    Posters,
    DirectorsImages,
    StudiosImages,
)
from movies.serializers import (
    MovieInfoSerializer,
    DirectorsSerializer,
    StudiosSerializer,
    DirectorsImagesSerializer,
    StudiosImagesSerializer,
)
from django.test import RequestFactory


@pytest.mark.django_db
def test_directors_images_serializer():
    # set up director
    director = Directors.objects.create(
        director_name="Christopher Nolan",
        nationality="British",
        director_date_of_birth="1970-07-30",
        director_best_movies="Inception, Interstellar, The Dark Knight",
        awards="Academy Award",
    )

    # Create a mock picture file
    picture_file = SimpleUploadedFile(
        "picture.jpg", b"file_content", content_type="image/jpeg"
    )
    picture = DirectorsImages.objects.create(director=director, picture=picture_file)

    # Create a request object to pass as context to the serializer
    request = RequestFactory().get("/")
    serializer_context = {"request": request}

    # Create the serializer with the director instance and context
    serializer = DirectorsSerializer(director, context=serializer_context)

    # Construct the expected data
    expected_data = {
        "id": director.id,
        "director_name": "Christopher Nolan",
        "nationality": "British",
        "director_date_of_birth": "1970-07-30",
        "director_best_movies": "Inception, Interstellar, The Dark Knight",
        "awards": "Academy Award",
        "picture_url": request.build_absolute_uri(picture.picture.url),
    }

    assert serializer.data == expected_data
