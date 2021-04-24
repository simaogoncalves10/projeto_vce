from .query import *
from .estimators import *
from .active_learning import ActiveLearner
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
import numpy as np
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from PIL import Image


class AnotationsViewSet(APIView):
    
    def get(self, request, format=None):
        try:
            #get active learning technic activated for training
            al=AL.objects.get(activated=True)

            #globals allows to call a function by a string  Ex: cnn() ->  globals()["cnn"]()
            model=globals()[al.model]()
            classifier = KerasClassifier(model)

            #globals allows to call a function by a string  Ex: UncertaintySampling(10) ->  globals()["cnn"](10)
            query_techinc=globals()[al.query_technic](al.n_instances)

            #load images
            unlabeled_dataset=UnlabeledDataset.objects.get(id_al=al.id)
            unlabeled_images=UnlabeledImage.objects.filter(id_dataset=unlabeled_dataset.id)

            images=[]
            for image in unlabeled_images: 
                image.image.open()
                img = np.array(Image.open(image.image))
                images.append(img)

            training_dataset=TrainingDataset.objects.get(id_al=al.id)
            training_images=TrainingImage.objects.filter(id_dataset=training_dataset.id)

            x_train = []
            y_train = []
            
            for image in training_images: 
                image.image.open()
                img = np.array(Image.open(image.image))
                x_train.append(img)

                if(image.label==True):
                    y_train.append(1)
                else:
                    y_train.append(0)
            
            learner = ActiveLearner(
                classifier,
                query_techinc,
                np.array(x_train),
                np.array(y_train)
            )

            print(learner)
            #get images to anotate
            index,instances=learner.get_images(np.array(images))

            #send zip file with images
            temp = tempfile.TemporaryFile()
            archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
            index=0
            for image in instances:
                index=index+1
                archive.write(image.path, 'file%d.png' % index)

            archive.close()

            temp.seek(0)
            wrapper = FileWrapper(temp)

            response = HttpResponse(wrapper, content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename=test.zip'
            return response
        except AL.DoesNotExist:
            raise Http404

            