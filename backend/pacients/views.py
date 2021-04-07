from rest_framework.viewsets import ModelViewSet
from .models import Pacient
from .serializers import PacientSerializer
from rest_framework import permissions

class PatiantsViewSet(ModelViewSet):
    queryset = Pacient.objects.all()
    serializer_class = PacientSerializer

    #É necessário estar autenticado para inserir informação e ver informação
    #permission_classes = (permissions.IsAuthenticated,)

