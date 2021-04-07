from django.db import models
from django.db.models import UniqueConstraint

class Pacient(models.Model):
    id_pacient = models.AutoField(unique=True, primary_key=True, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    birth_date = models.DateField(null=False)
    total_exams = models.IntegerField(unique=True, null=False)

    gender_male = 0
    gender_female = 1
    gender_not_to_say = 2
    gender_choices = [(gender_male, 'Male'), (gender_female, 'Female'), (gender_not_to_say, 'Prefer not to say')]
    gender = models.IntegerField(choices=gender_choices)
    
    remarks = models.TextField(max_length=1000, null=False)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['id_pacient']