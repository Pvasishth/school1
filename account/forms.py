from .models import *
from schoolclasses.models import *
from student.models import StudentProfile
from django.forms.widgets import DateInput
# from django.contrib.auth.forms import UserCreationForm

##################################################################
# accounts.forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('__all__')
        exclude = ('last_login',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('__all__')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
####################################################################
# class StudentSignUpForm(forms.ModelForm):
#     class Meta():
#         model = User
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_student = True
#         if commit:
#             user.save()
#         return user
#
#
# class TeacherSignUpForm(forms.ModelForm):
#     class Meta():
#         model = User
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_teacher = True
#         if commit:
#             user.save()
#         return user
#
# class PrincipalSignUpForm(forms.ModelForm):
#     class Meta():
#         model = User
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_principal = True
#         if commit:
#             user.save()
#         return user
#


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

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



class Class_Add_form(forms.ModelForm):
  class Meta:
    model = Class
    fields = '__all__'

class StudentProfileForm(forms.ModelForm):
  class Meta:
    model = StudentProfile
    fields = '__all__'
    exclude=('student',)
    widgets = {
        'date_of_birth': DateInput(attrs={'type': 'date'}),

    }




