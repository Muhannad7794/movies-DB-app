from rest_framework.routers import DefaultRouter
from .views import MovieInfoViewSet, DirectorsViewSet, StudiosViewSet

router = DefaultRouter()
router.register(r'movies', MovieInfoViewSet)
router.register(r'directors', DirectorsViewSet)
router.register(r'studios', StudiosViewSet)

urlpatterns = router.urls
