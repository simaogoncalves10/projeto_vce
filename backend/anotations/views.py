from .query import *
from .estimators import *
from als.models import AL
from als.serializers import ALSerializer
from training.models import TrainingDataset,TrainingImage
from training.serializers import TrainingDatasetSerializer, TrainingImageSerializer
from testing.models import TestingDataset,TestingImage
from testing.serializers import TestingDatasetSerializer, TestingImageSerializer
from unlabeled.models import UnlabeledDataset,UnlabeledImage
from unlabeled.serializers import UnlabeledDatasetSerializer, UnlabeledImageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
import tempfile, zipfile
from django.http import HttpResponse
from wsgiref.util import FileWrapper

class AnotationsViewSet(APIView):
    
    def get(self, request, format=None):
        try:
            al=AL.objects.get(activated=True)
            
            dataset=UnlabeledDataset.objects.get(id_al=al.id)
            filtered_images=UnlabeledImage.objects.filter(id_dataset=dataset.id)
            serializer = UnlabeledImageSerializer(filtered_images, many=True)
            #return Response(serializer.data)


            temp = tempfile.TemporaryFile()
            archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
            index=0
            for image in filtered_images:
                index=index+1

                archive.write(image.image.path, 'file%d.png' % index) # 'file%d.png' will be the
                                                            # name of the file in the
                                                            # zip
            archive.close()

            temp.seek(0)
            wrapper = FileWrapper(temp)

            response = HttpResponse(wrapper, content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename=test.zip'
            return response
        except AL.DoesNotExist:
            raise Http404