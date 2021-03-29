from rest_framework.viewsets import ModelViewSet
from .models import pacient
from .serializers import PacientSerializer

class PatiantsViewSet(ModelViewSet):
    queryset = pacient.objects.all()
    serializer_class = PacientSerializer

