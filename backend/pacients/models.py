from django.db import models
from django.db.models import UniqueConstraint

class pacient(models.Model):
    IDPacient = models.AutoField(unique=True, primary_key=True, null=False)
    IDPacientAnonym = models.IntegerField(unique=True, null=False)
    FirstName = models.CharField(max_length=50, null=False)
    LastName = models.CharField(max_length=50, null=False)
    BirthDate = models.DateField(null=False)
    Gender = models.CharField(max_length=50, null=False) #Masculinho, Feminino, prefiro não divulgar
    TotalExams = models.IntegerField(unique=True, null=False)
    Remarks = models.TextField(max_length=1000, null=False)

    def __str__(self):
        return self.FirstName

    class Meta:
        #Chave primária composta
        ordering = ['IDPacient']
        UniqueConstraint(fields = ['IDPacient', 'IDPacientAnonym'], name = 'IDPacient_CPK') #CPK = Composite Primary Key