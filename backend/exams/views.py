from rest_framework.viewsets import ModelViewSet
from .models import exam
from .serializers import ExamSerializer

class ExamViewSet(ModelViewSet):
    queryset = exam.objects.all()
    serializer_class = ExamSerializer