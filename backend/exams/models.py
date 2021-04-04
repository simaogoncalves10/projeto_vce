from django.db import models
from backend.pacients.models import pacient

class Exam(models.Model):
    id_exam = models.AutoField(unique=True, primary_key=True, null=False)
    id_pacient_anonym = models.ForeignKey(pacient, on_delete=models.CASCADE, default = None) #on_delete serve para caso um paciente seja removido, os exames serem removidos (e nunca vice-versa)
    exam_date = models.DateField(max_length=100, null=False)
    exam_type = models.CharField(max_length=100, null=False)
    exam_notes = models.TextField(max_length=1000, null=False)
    exam_result = models.TextField(max_length=1000, null=False)

    
    def __str__(self):
        return str(self.id_exam)

    class Meta:
        ordering = ['id_exam']