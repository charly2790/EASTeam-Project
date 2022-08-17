from re import T
from turtle import title
from django.db import models

class Settings(models.Model):
    title = models.CharField(max_length=50,blank=True,null=True)
    description = models.CharField(max_length=60,blank=True,null=True)
    value =  models.TextField(blank=True,null=True)

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = "Settings"
