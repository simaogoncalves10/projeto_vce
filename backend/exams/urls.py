from django.urls import path
from rest_framework import routers
from .views import ExamViewSet

router = routers.DefaultRouter()
router.register('exams', ExamViewSet)

urlpatterns = router.urls

