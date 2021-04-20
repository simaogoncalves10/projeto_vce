from rest_framework import serializers
from .models.testing import TestingDataset, TestImage


class TestingDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingDataset
        fields = '__all__'


class TestImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestImage
        fields = '__all__'


