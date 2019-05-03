from.models import *
from django import forms
from django.forms.widgets import DateInput
from django.contrib.auth.forms import AuthenticationForm


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
            'joining_date': DateInput(attrs={'type': 'date'}),

        }

class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_teacher:
            raise forms.ValidationError('This is only for Teacher login page', code='inactive')
