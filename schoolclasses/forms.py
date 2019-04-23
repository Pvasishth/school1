from django import forms
from.models import *



class class_add_form(forms.ModelForm):
    class Meta:
        model = Class
        fields='__all__'



class section_add_form(forms.ModelForm):
    class Meta:
        model = section
        fields = '__all__'