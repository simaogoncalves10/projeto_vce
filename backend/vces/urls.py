from django.db.models import base
from rest_framework import routers
from .views import VCEViewSet

router = routers.DefaultRouter()
router.register('vces', VCEViewSet)

urlpatterns = router.urls