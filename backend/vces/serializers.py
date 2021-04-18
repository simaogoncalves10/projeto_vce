from rest_framework import serializers
from .models import VCE


class VCESerializer(serializers.ModelSerializer):
    class Meta:
        model = VCE
        fields = "__all__"