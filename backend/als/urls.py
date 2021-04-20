from rest_framework import routers
from .views import ALsViewSet

router = routers.DefaultRouter()
router.register('als', ALsViewSet)

urlpatterns = router.urls