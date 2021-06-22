from django import forms
from django.forms import widgets
from . models import *
class CreateForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ("project_name", "type", "langvage")

        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'langvage': forms.TextInput(attrs={'class': 'form-control'}),
        }

