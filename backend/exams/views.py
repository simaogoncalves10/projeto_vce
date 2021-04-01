from rest_framework.viewsets import ModelViewSet
from .models import exam
from .serializers import ExamSerializer
from rest_framework import permissions

class ExamViewSet(ModelViewSet):
    queryset = exam.objects.all()
    serializer_class = ExamSerializer

    #É necessário estar autenticado para inserir informação e ver informação
    permission_classes = (permissions.IsAuthenticated,)