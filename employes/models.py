from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField

class Teacher(models.Model):

  GENDER_CHOICES  = (('male','MALE'),('female','FEMALE'))
  SUBJECT_CHOICES = (('english','ENGLISH'),('hindi','HINDI'),('maths','MATHS'),('science','SCIENCE'),
                    ('social science','SOCIAL_SCIENCE'))
  CLASSES_CHOICES = (('nur', 'NUR'),('lkg','LKG'),('ukg','UKG'),('1st','1ST'),('2nd','2nd'),('3rd','3rd'),('4th','4th'),('5th','5th'),('6th','6th'),('7th','7th'),
                    ('8th','8th'),('9th','9th'),('10th','10th'),('11th','11th'),('12th','12th'))


  full_name = models.CharField(max_length=20,default=True)
  username = models.CharField(max_length=15,default=True, unique=True)
  age = models.PositiveSmallIntegerField(default=1)
  gender = models.CharField(max_length=10,default=True,choices=GENDER_CHOICES)
  date_of_birth = models.DateField(max_length=8,default=True)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '8885559997'. Up to 12 digits allowed along with country code.")
  mobile_number = models.CharField(validators=[phone_regex],default=True, max_length=12)
  subject_expertise =MultiSelectField(choices=SUBJECT_CHOICES,default=True)
  experience = models.PositiveSmallIntegerField(default=True)
  joining_date = models.DateField(max_length=8,default=True)
  email_id = models.EmailField(default=True)
  highest_qualification = models.CharField(max_length=20,default=True)

  def __str__(self):
    return self.full_name
