import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory
from django.core.files.base import ContentFile

from movies.models import Directors, DirectorsImages


@pytest.mark.django_db
def test_directorsImages_model():
    # set up director
    director = Directors.objects.create(
        director_name="Martin Scorsese",
        nationality="American",
        director_date_of_birth="1942-11-17",
        director_best_movies="Goodfellas, Taxi Driver, The Departed",
        awards="Academy Award",
    )

    # create a mock image file
    image_content = b"file_content"
    image_file = SimpleUploadedFile(
        "image.jpg", image_content, content_type="image/jpeg"
    )
    # create an image instance
    image = DirectorsImages.objects.create(director=director, picture=image_file)
    # assert that the image is created and the director has an image
    assert DirectorsImages.objects.count() == 1
    # assert the values of the image
    assert image.director == director

    # read the content of the saved image file for comparison
    saved_image_content = image.picture.read()

    # assert the content of the saved file matches the original content
    assert saved_image_content == image_content

    # assert that the image object has a file associated with it
    assert image.picture is not None
