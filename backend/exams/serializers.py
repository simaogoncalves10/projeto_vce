from rest_framework.serializers import ModelSerializer
from .models import exam

class ExamSerializer(ModelSerializer):
    class Meta:
        model = exam
        fields = ['IDExam', 'ExamDate', 'ExamType', 'ExamNotes', 'ExamResult']

    #IDPacientAnonym = models.ForeignKey(pacients.pacients, on_delete=models.CASCADE, default = None, IDPacientAnonym) #on_delete serve para caso um paciente seja removido, os exames serem removidos (e nunca vice-versa)