from rest_framework import serializers
from .models import Endoscopy,Image


class EndoscopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Endoscopy
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image 
        fields = '__all__'


