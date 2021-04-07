from rest_framework.viewsets import ModelViewSet
from .models import Exam
from .serializers import ExamSerializer
from rest_framework import permissions

class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    #É necessário estar autenticado para inserir informação e ver informação
    #permission_classes = (permissions.IsAuthenticated,)