from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from account.models import User
from schoolclasses.models import *


class StudentProfile(models.Model):
    student_name = models.CharField(max_length=20)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='student_class')
    student_section = models.ForeignKey(Section, null=True,blank=True, on_delete=models.CASCADE, related_name='student_section')
    student_roll_number = models.PositiveIntegerField()
    student_reg_number = models.CharField(max_length=20)
    student_previous_school = models.CharField(max_length=20)
    student_previous_school_transfer_certificate = models.ImageField(null=True,blank=True)
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '8885559997'. Up to 12 digits allowed along with country code.")
    guardian_mobile_number = models.CharField(validators=[phone_regex], max_length=12)
    parents_email_id = models.EmailField()
    student_email_id = models.EmailField()
    family_photo = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField()
    home_address = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.student_name



