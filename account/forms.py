from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import SchoolProfile,MediaUpload,Alert


##################################################################################################33
from .models import User
from django.contrib.auth.forms import UserCreationForm


class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user

class PrincipalSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_principal = True
        if commit:
            user.save()
        return user

####################################################################################################3


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
