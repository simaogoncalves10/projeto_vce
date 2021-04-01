from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class user(AbstractUser): 
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    
    Medic_Yes = 0
    Medic_NO = 1
    MEDIC_CHOICES = [(Medic_Yes, 'Sim'), (Medic_NO, 'Nao')]
    medic = models.IntegerField(choices=MEDIC_CHOICES, default=1)


    REQUIRED_FIELDS = ('first_name', 'last_name', 'email', 'medic')

    USERNAME_FIELD = 'username'

    
    #Dar as permissões do grupo médico, caso seja médico
    '''
    if (user.is_medic == True):
        medic_group = Group.objects.get(name = 'Medic')
        user.groups.add(medic_group)
    '''   

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']