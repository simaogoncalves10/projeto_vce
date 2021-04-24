from django.urls import path
from .views import *

app_name = 'endoscopies'

urlpatterns = [
    path('endoscopies/', Endoscopy_APIView.as_view()),
    path('endoscopies/<int:id>/', Endoscopy_APIView_Detail.as_view()), 
]