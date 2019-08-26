from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    is_medico = models.BooleanField('medico', default=False)
    is_paciente = models.BooleanField('paciente', default=False)
 
