from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TestingDatasetSerializer, TestingImageSerializer
from .models import TestingDataset, TestingImage
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
    
    
class Testing_APIView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request, format=None, *args, **kwargs):
        dataset = TestingDataset.objects.all()
        serializer = TestingDatasetSerializer(dataset, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        testing_serializer = TestingDatasetSerializer(data=request.data)
        if testing_serializer.is_valid() and request.data['informative_images'] and request.data['informative_images']:
            testing=testing_serializer.save()

            serializer = TestingDatasetSerializer(data=request.data)
            
            informative_list = request.FILES.getlist('informative_images')
            non_informative_list = request.FILES.getlist('non_informative_images')
            if serializer.is_valid():
                for item in informative_list:
                    f = TestingImage.objects.create(image=item, id_dataset=testing, label=True)
                for item in non_informative_list:
                    f = TestingImage.objects.create(image=item, id_dataset=testing, label=False)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

class Testing_APIView_Detail(APIView):
    serializer_class = TestingImageSerializer

    def get(self, request, id, format=None):
        try:
            if TestingDataset.objects.get(pk=id):
                    filtered_images=TestingImage.objects.filter(id_dataset=id)
                    serializer = TestingImageSerializer(filtered_images, many=True)
                    return Response(serializer.data)
        except TestingDataset.DoesNotExist:
            raise Http404
        
    def delete(self, request, id, format=None):
        try:
            if TestingDataset.objects.get(pk=id):
                filtered_images=TestingImage.objects.filter(id_dataset=id)
                filtered_images.delete()
            testing = TestingDataset.objects.get(pk=id)
            testing.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TestingDataset.DoesNotExist:
            raise Http404
        