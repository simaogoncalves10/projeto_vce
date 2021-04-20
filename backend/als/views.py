from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AL
from .serializers import ALSerializer
from rest_framework import status
from django.http import Http404

class ALsViewSet(APIView):
    
    def get(self, request, format=None, *args, **kwargs):
        al = AL.objects.all()
        serializer = ALSerializer(al, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        al_serializer = ALSerializer(data=request.data)

        if al_serializer.is_valid():
            al=al_serializer.save()
            return Response(al_serializer.data, status=status.HTTP_201_CREATED)
        return Response(al_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AL_APIView_Detail(APIView):
    serializer_class = ALSerializer
    
    def get_object(self, pk):
        try:
            return AL.objects.get(pk=pk)
        except AL.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        al = self.get_object(pk)
        serializer = ALSerializer(al)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        al = self.get_object(pk)
        serializer = ALSerializer(al, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        al = self.get_object(pk)
        al.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
class ActivateALsViewSet(APIView):
    def get(self, request, format=None):
        try:
            al=AL.objects.get(activated=True)
            serializer = ALSerializer(al)
            return Response(serializer.data)
        except AL.DoesNotExist:
            raise Http404


class ActivateALsViewSet_Detail(APIView):

    def get(self, request, pk, format=None):
        
        try:
            to_desactivate=AL.objects.get(activated=True)
            to_desactivate.activated = False

            to_activate=AL.objects.get(id=pk)
            to_activate.activated = True
            
            to_desactivate.save() 
            to_activate.save() 
  

            serializer = ALSerializer(to_activate)

            return Response(serializer.data)
        except AL.DoesNotExist:
            raise Http404            
        

        
        