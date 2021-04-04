from rest_framework.serializers import ModelSerializer
from .models import Pacient

class PacientSerializer(ModelSerializer):
    class Meta:
        model = Pacient
        fields = ['id_pacient', 'first_name', 'last_name', 'birth_date', 'gender', 'total_exams', 'remarks']