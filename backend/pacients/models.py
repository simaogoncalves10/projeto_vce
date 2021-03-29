from django.db import models
from django.db.models import UniqueConstraint

class pacient(models.Model):
    IDPacient = models.AutoField(unique=True, primary_key=True, null=False)
    IDPacientAnonym = models.IntegerField(unique=True, null=False)
    FirstName = models.CharField(max_length=50, null=False)
    LastName = models.CharField(max_length=50, null=False)
    BirthDate = models.DateField(null=False)
    
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_NOTTOSAY = 2
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'), (GENDER_NOTTOSAY, 'Prefer not to say')]
    Gender = models.IntegerField(choices=GENDER_CHOICES)

    #Gender = models.CharField(max_length=50, null=False) #Masculinho, Feminino, prefiro não divulgar
    
    TotalExams = models.IntegerField(unique=True, null=False)
    Remarks = models.TextField(max_length=1000, null=False)

    def __str__(self):
        return self.FirstName

    class Meta:
        #Chave primária composta
        ordering = ['IDPacient']
        UniqueConstraint(fields = ['IDPacient', 'IDPacientAnonym'], name = 'IDPacient_CPK') #CPK = Composite Primary Key