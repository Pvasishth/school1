from django import forms
from.models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget




class class_add_form(forms.ModelForm):
    class Meta:
        model = Class
        fields='__all__'



class section_add_form(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

        content = forms.CharField(widget=CKEditorUploadingWidget())
