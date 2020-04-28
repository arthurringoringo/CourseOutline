from django import forms
from .models import *
from django.forms import ModelForm

class CreateForm(forms.ModelForm):
    class Meta:
        model = CourseOutline
        fields = '__all__'