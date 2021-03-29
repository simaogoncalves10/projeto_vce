from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser): 
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    REQUIRED_FIELDS = ('first_name', 'last_name', 'email')
    #Será mais fácil adicionar booleanos depois para as premissões
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']