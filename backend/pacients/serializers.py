from rest_framework.serializers import ModelSerializer
from .models import pacient

class PacientSerializer(ModelSerializer):
    class Meta:
        model = pacient
        fields = ['IDPacient', 'IDPacientAnonym', 'FirstName', 'LastName', 'BirthDate', 'Gender', 'TotalExams', 'Remarks']