from.models import *
from django import forms
from django.forms.widgets import DateInput



class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
            'joining_date': DateInput(attrs={'type': 'date'}),

        }
