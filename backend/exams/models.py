from django.db import models
#from pacients import models

class exam(models.Model):
    IDExam = models.AutoField(unique=True, primary_key=True, null=False)
    #IDPacientAnonym = models.ForeignKey(pacients.pacients, on_delete=models.CASCADE, default = None, IDPacientAnonym) #on_delete serve para caso um paciente seja removido, os exames serem removidos (e nunca vice-versa)
    ExamDate = models.DateField(max_length=100, null=False)
    ExamType = models.CharField(max_length=100, null=False)
    ExamNotes = models.TextField(max_length=1000, null=False)
    ExamResult = models.TextField(max_length=1000, null=False)

    


    def __str__(self):
        return str(self.IDExam)

    class Meta:
        ordering = ['IDExam']