from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AL
from .serializers import ALSerializer

class ALsViewSet(ModelViewSet):
    queryset = AL.objects.all()
    serializer_class = ALSerializer


# class ListUsers(APIView):
#     def get(self, request, format=None):
#         return Response("HELLO WORLD")