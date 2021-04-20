from rest_framework.viewsets import ModelViewSet
from .models import AL
from .serializers import ALSerializer

class ALsViewSet(ModelViewSet):
    queryset = AL.objects.all()
    serializer_class = ALSerializer