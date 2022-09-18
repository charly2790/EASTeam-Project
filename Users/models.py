from django.db import models
from django.contrib.auth.models import User
from allauth import socialaccount
# Create your models here.

class Profile (models.Model):
    photo = models.URLField(blank=True, null=True)
