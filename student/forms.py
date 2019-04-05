from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):
  class Meta:
    model = StudentProfile
    fields = '__all__'
