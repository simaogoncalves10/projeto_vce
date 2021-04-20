from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ImageSerializer, EndoscopySerializer
from .models import Image, Endoscopy
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
    
    
class Endoscopy_APIView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request, format=None, *args, **kwargs):
        endoscopy = Endoscopy.objects.all()
        serializer = EndoscopySerializer(endoscopy, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        endoscopy_serializer = EndoscopySerializer(data=request.data)
        if endoscopy_serializer.is_valid() and request.data['images']:
            endoscopy=endoscopy_serializer.save()

            serializer = ImageSerializer(data=request.data)
            
            files_list = request.FILES.getlist('images')
            if serializer.is_valid():
                for item in files_list:
                    f = Image.objects.create(image=item, id_endoscopy=endoscopy)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

class Endoscopy_APIView_Detail(APIView):
    serializer_class = ImageSerializer

    def get(self, request, id, format=None):
        try:
            if Endoscopy.objects.get(pk=id):
                    filtered_images=Image.objects.filter(id_endoscopy=id)
                    serializer = ImageSerializer(filtered_images, many=True)
                    return Response(serializer.data)
        except Endoscopy.DoesNotExist:
            raise Http404
        
    def delete(self, request, id, format=None):
        try:
            if Endoscopy.objects.get(pk=id):
                filtered_images=Image.objects.filter(id_endoscopy=id)
                filtered_images.delete()
            endoscopy = Endoscopy.objects.get(pk=id)
            endoscopy.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Endoscopy.DoesNotExist:
            raise Http404
        