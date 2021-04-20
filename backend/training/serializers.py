from rest_framework import serializers
from .models.training import TrainingDataset, TrainImage


class TrainingDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingDataset
        fields = '__all__'


class TrainImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainImage
        fields = '__all__'


