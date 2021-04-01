from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class user(AbstractUser): 
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)

    NOT_MEDIC = 0
    IS_MEDIC = 1
    MEDIC_CHOICES = [(NOT_MEDIC, 'No'), (IS_MEDIC, 'Yes')]
    Medic = models.IntegerField(choices=MEDIC_CHOICES)
    
    REQUIRED_FIELDS = ('first_name', 'last_name', 'email', 'Medic')

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