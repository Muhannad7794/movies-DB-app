from django.contrib import admin
from .models import (
    MovieInfo,
    Directors,
    Studios,
    Posters,
    DirectorsImages,
    StudiosImages,
)

# Register your models here.
admin.site.register(MovieInfo)
admin.site.register(Directors)
admin.site.register(Studios)
admin.site.register(Posters)
admin.site.register(DirectorsImages)
admin.site.register(StudiosImages)
