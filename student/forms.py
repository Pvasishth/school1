from django.forms.widgets import DateInput
from django import forms
from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):
  class Meta:
    model = StudentProfile
    fields = '__all__'
    exclude=('student',)
    widgets = {
    'date_of_birth': DateInput(attrs={'type': 'date'}),
     }