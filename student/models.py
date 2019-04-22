from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from account.models import User
from schoolclasses.models import *


class StudentProfile(models.Model):
    student_name = models.CharField(max_length=20, null=True, blank=True)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    student_section = models.ForeignKey(section, on_delete=models.CASCADE)
    student_roll_number = models.CharField(max_length=10, null=True, blank=True)
    student_reg_number = models.CharField(max_length=20, null=True, blank=True)
    student_previous_school = models.CharField(max_length=20, null=True, blank=True)
    student_previous_school_transfer_certificate = models.ImageField(default=False)
    student_batch_no = models.CharField(max_length=20, null=True, blank=True)
    father_name = models.CharField(max_length=20, null=True, blank=True)
    mother_name = models.CharField(max_length=20, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '8885559997'. Up to 12 digits allowed along with country code.")
    guardian_mobile_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    parents_email_id = models.EmailField(null=True, blank=True)
    student_email_id = models.EmailField(null=True, blank=True)
    # family_photo = models.ImageField(default=False)
    # date_of_birth = models.DateField(null=True, blank=True)
    home_address = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.student_name



