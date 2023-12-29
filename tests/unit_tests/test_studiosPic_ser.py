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
def test_studios_images_serializer():
    # set up studio
    studio = Studios.objects.create(
        name="Warner Bros",
        founded=1923,
        location="Burbank, California",
    )

    # Create a mock picture file
    picture_file = SimpleUploadedFile(
        "picture.jpg", b"file_content", content_type="image/jpeg"
    )
    picture = StudiosImages.objects.create(studio=studio, picture=picture_file)

    # Create a request object to pass as context to the serializer
    request = RequestFactory().get("/")
    serializer_context = {"request": request}

    # Create the serializer with the studio instance and context
    serializer = StudiosSerializer(studio, context=serializer_context)

    # Construct the expected data
    expected_data = {
        "id": studio.id,
        "name": "Warner Bros",
        "founded": 1923,
        "location": "Burbank, California",
        "picture_url": request.build_absolute_uri(picture.picture.url),
    }

    assert serializer.data == expected_data
