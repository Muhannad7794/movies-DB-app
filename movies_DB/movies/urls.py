from rest_framework.routers import DefaultRouter
from .views import MovieInfoViewSet, DirectorsViewSet, StudiosViewSet, PostersViewSet

router = DefaultRouter()
router.register(r"movies", MovieInfoViewSet)
router.register(r"directors", DirectorsViewSet)
router.register(r"studios", StudiosViewSet)
router.register(r"posters", PostersViewSet)

urlpatterns = router.urls

