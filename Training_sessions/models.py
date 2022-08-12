from email.policy import default
from tabnanny import verbose
from django.db import models
from django.forms import BooleanField, FloatField, TimeField, URLField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Training_type(models.Model):
    name = models.CharField(max_length=40,blank =False, null=False)
    description = models.TextField(null = False)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name
    
    class Meta:
            verbose_name = 'Tipo de Entrenamiento'
            verbose_name_plural = "Tipos de Entrenamiento"

class Rpe(models.Model):
    name = models.CharField(max_length=40,blank = False, null = False)
    description = models.TextField(null = False)

class Training_session(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    dt_assign = models.DateTimeField()
    tr_type = models.ForeignKey(Training_type,on_delete = models.CASCADE)
    target = models.TextField(null = False)
    training = models.TextField()
    distance = models.FloatField()
    time = models.TimeField()
    done = models.BooleanField(default=False)
    rpe = models.ForeignKey(Rpe,on_delete=models.CASCADE)
    url = models.URLField()
    






