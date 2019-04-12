from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import SchoolProfile,MediaUpload,Alert

class UserRegistrationForm(forms.ModelForm):


    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

    def clean_password2(self):

        cd = self.cleaned_data
        if cd['password'] != cd['password2'] :
            raise forms.ValidationError('PASSWORD DOESN\'T MATCH')

        return cd  

class MediaUploadForm(forms.ModelForm):
  class Meta:
    model = MediaUpload
    fields = '__all__'
    exclude = ('SchoolProfile',)

class SchoolProfileForm(forms.ModelForm):
  class Meta:
    model = SchoolProfile
    fields = '__all__'
    exclude = ('principal',)


class Alert_form(forms.ModelForm):
    class Meta:
        model = Alert
        fields = '__all__'
