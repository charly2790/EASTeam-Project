from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Training_type,Training_session,Rpe

class Training_typeForm(ModelForm):
    class Meta:
        model = Training_type
        fields = "__all__"

class Training_sessionForm(ModelForm):
    class Meta:
        model = Training_session
        fields = "__all__"

class RpeForm(ModelForm):
    class Meta:
        model = Rpe
        fields = "__all__"