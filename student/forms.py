from django.forms.widgets import DateInput
from django import forms
from .models import StudentProfile
from django.contrib.auth.forms import AuthenticationForm


class StudentProfileForm(forms.ModelForm):
  class Meta:
    model = StudentProfile
    fields = '__all__'
    exclude=('student',)
    widgets = {
    'date_of_birth': DateInput(attrs={'type': 'date'}),
     }



class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
      if not user.is_student:
        raise forms.ValidationError('This is only for Student login page', code='inactive')
