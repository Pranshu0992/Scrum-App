from rest_framework.routers import DefaultRouter

from .api import ListViewSet, CardViewSet


router = DefaultRouter()

router.register(r'lists', ListViewSet)
router.register(r'card', CardViewSet)

urlpatterns = router.urls