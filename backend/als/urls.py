from rest_framework import routers
from .views import ALsViewSet#, ListUsers

router = routers.DefaultRouter()
router.register('als', ALsViewSet)
#router.register('als/acivate', ListUsers.as_view())


urlpatterns = router.urls