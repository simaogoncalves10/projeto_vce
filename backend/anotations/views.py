from .query import *
from .estimators import *
from modAL.models import ActiveLearner
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

    def zip(self,index,unlabeled_dataset):
            #send zip file with images
            temp = tempfile.TemporaryFile()
            archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)


            for idx in index:
                image=UnlabeledImage.objects.filter(id_dataset=unlabeled_dataset.id,blocked=False)[int(idx)]
                image.blocked=True
                image.save()
                archive.write(image.image.path, '%d.png' % image.id)

            archive.close()

            temp.seek(0)
            wrapper = FileWrapper(temp)

            response = HttpResponse(wrapper, content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename=unlabeled.zip'
            return response
        
    def load_images(self,unlabeled_dataset,training_dataset):
            unlabeled_images=UnlabeledImage.objects.filter(id_dataset=unlabeled_dataset.id, blocked=False)

            pool=[]
            #unlabeled_images to numpy  
            for image in unlabeled_images: 
                image.image.open()
                img = np.array(Image.open(image.image).convert("RGB"))
                pool.append(img)
            
            training_images=TrainingImage.objects.filter(id_dataset=training_dataset.id)

            x_train, y_train = [], []  
            #training_images to numpy      
            for image in training_images: 
                image.image.open()
                img = np.array(Image.open(image.image).convert("RGB"))
                x_train.append(img)

                if(image.label==True):
                    y_train.append(1)
                else:
                    y_train.append(0)

            return pool, x_train, y_train
    
    def get(self, request, format=None):
        try:
            #get active learning technic activated for training
            al=AL.objects.get(training_activated=True)
  
            if(al.is_quering): return Response("Try later please, get anotations is busy. This helps avoid concurrency")
            else:
                al.is_quering=True
                al.save()
                
                #globals allows to call a function by a string  Ex: cnn ->  globals()["cnn"]
                model=globals()[al.model]
                classifier = KerasClassifier(model)
                
                #globals allows to call a function by a string  Ex: UncertaintySampling(10) ->  globals()["cnn"](10)
                query_techinc=globals()[al.query_technic](al.n_instances)
        
                #load images
                unlabeled_dataset=UnlabeledDataset.objects.get(id_al=al.id)
            
                #get training images from this al
                training_dataset=TrainingDataset.objects.get(id_al=al.id)
            
                pool, x_train, y_train = self.load_images(unlabeled_dataset,training_dataset)
                
                #create modal framework active learning instance
                learner = ActiveLearner(
                    classifier,
                    query_techinc,
                    np.array(x_train,dtype = float),
                    np.array(y_train,dtype = float)
                )
    
                #get images to anotate
                index,_=learner.query(np.array(pool))

                al.is_quering=False
                al.save()
                # return response with zip file with images
                return self.zip(index,unlabeled_dataset)
        except AL.DoesNotExist:
            raise Http404


            