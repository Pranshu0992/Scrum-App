from .api import ListViewSet, CardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'lists', ListViewSet)
router.register(r'card', CardViewSet)

urlpatterns = router.urls