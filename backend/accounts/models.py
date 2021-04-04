from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser): 
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    
    medic_no = 0
    medic_yes = 1
    medic_choices = [(medic_no, 'No'), (medic_yes, 'Yes')]
    medic = models.IntegerField(choices=medic_choices, default=1)


    REQUIRED_FIELDS = ('first_name', 'last_name', 'email', 'medic')

    USERNAME_FIELD = 'username'

    
    #Dar as permissões do grupo médico, caso seja médico
    '''
    if (medic == 1):
        user.groups.add(Group.)
        pass
    '''
    '''
    if (user.is_medic == True):
        medic_group = Group.objects.get(name = 'Medic')
        user.groups.add(medic_group)
    ''' 

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']