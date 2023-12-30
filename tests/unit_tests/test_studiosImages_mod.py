import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory
from django.core.files.base import ContentFile

from movies.models import Studios, StudiosImages


@pytest.mark.django_db
def test_studiosImages_model():
    # set up studio
    studio = Studios.objects.create(
        name="Warner Bros",
        founded=1923,
        location="Burbank, California",
    )

    # create a mock image file
    image_content = b"file_content"
    image_file = SimpleUploadedFile(
        "image.jpg", image_content, content_type="image/jpeg"
    )
    # create an image instance
    image = StudiosImages.objects.create(studio=studio, picture=image_file)
    # assert that the image is created and the studio has an image
    assert StudiosImages.objects.count() == 1
    # assert the values of the image
    assert image.studio == studio

    # read the content of the saved image file for comparison
    saved_image_content = image.picture.read()

    # assert the content of the saved file matches the original content
    assert saved_image_content == image_content

    # assert that the image object has a file associated with it
    assert image.picture is not None
