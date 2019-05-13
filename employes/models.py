from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from django.conf import settings

user = settings.AUTH_USER_MODEL

class Teacher(models.Model):

  GENDER_CHOICES  = (('male','MALE'),('female','FEMALE'))
  SUBJECT_CHOICES = (('english','ENGLISH'),('hindi','HINDI'),('maths','MATHS'),('science','SCIENCE'),
                    ('social science','SOCIAL_SCIENCE'))
  full_name = models.CharField(max_length=20)
  user = models.OneToOneField(user,on_delete=models.CASCADE,null=True,blank=True,related_name='teacher_profile')
  age = models.PositiveSmallIntegerField()
  gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
  date_of_birth = models.DateField(max_length=8,blank=True,null=True)
  address = models.TextField(default='No address',null=True)
  bio = models.TextField(default='No bio', null=True)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '8885559997'. Up to 12 digits allowed along with country code.")
  mobile_number = models.CharField(validators=[phone_regex],max_length=12)
  subject_expertise =MultiSelectField(choices=SUBJECT_CHOICES)
  experience = models.PositiveSmallIntegerField()
  joining_date = models.DateField(max_length=8,blank=True,null=True)
  email_id = models.EmailField()
  highest_qualification = models.CharField(max_length=20)

  def __str__(self):
    return self.full_name
