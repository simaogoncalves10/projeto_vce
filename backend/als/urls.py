from django.urls import path
from .views import ALsViewSet, AL_APIView_Detail, ActivateALsViewSet, ActivateALsViewSet_Detail
app_name = 'als'

urlpatterns = [
    path('als/', ALsViewSet.as_view()),
    path('als/<int:pk>/', AL_APIView_Detail.as_view()),
    path('als/activated/', ActivateALsViewSet.as_view()),    
    path('als/activated/<int:pk>/', ActivateALsViewSet_Detail.as_view()), 
]