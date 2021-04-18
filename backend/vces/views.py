from rest_framework.viewsets import ModelViewSet
from .models import VCE
from .serializers import VCESerializer


class VCEViewSet(ModelViewSet):
    queryset = VCE.objects.all()
    serializer_class = VCESerializer

   