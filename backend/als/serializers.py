from rest_framework import serializers
from .models import AL


class ALSerializer(serializers.ModelSerializer):
    class Meta:
        model = AL
        fields = '__all__'