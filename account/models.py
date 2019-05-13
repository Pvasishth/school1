from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from django.utils import timezone
from employes.models import *
from datetime import datetime
from django.contrib.auth.models import (
  AbstractUser)





class User(AbstractUser):
   is_principal = models.BooleanField(default=False)
   is_teacher = models.BooleanField(default=False)
   is_student = models.BooleanField(default=False)


class SchoolProfile(models.Model):
  principal = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'schoolprofile')
  school_name = models.CharField(max_length = 20)
  # username = models.CharField(max_length=25, unique=True)
  password = models.CharField(max_length=30)
  #address for the school
  state = models.CharField(max_length = 20)
  city = models.CharField(max_length = 20)
  area = models.CharField(max_length = 20)
  pincode = models.PositiveIntegerField(null=True)
  landmark = models.CharField(max_length = 20)

  #phone number field
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '88855599test@gmail.com97'. Up to 12 digits allowed along with country code.")
  phone_number = models.CharField(validators=[phone_regex], max_length=12)

  #school website
  website = models.URLField(null = True , blank = True)

#for uploading the media by the school 

class MediaUpload(models.Model):
  SchoolProfile = models.ForeignKey(SchoolProfile,on_delete = models.CASCADE, related_name = 'MediaUpload')

  Title = models.CharField(max_length=50, default=True)
  Message = models.TextField(default=True)
  Date = models.DateField(default=timezone.now)
  #images
  cover_photo = models.ImageField(null = True , blank = True)
  photo1 = models.ImageField(null = True , blank = True)
  photo2 = models.ImageField(null = True , blank = True)
  #videos
  video1 = models.URLField(null = True , blank = True)
  video2 = models.URLField(null = True , blank = True)
  #files
  school_brouche = models.FileField(null = True , blank = True)


class Alert(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField()
    image = models.ImageField(null=True,blank=True,upload_to='alert_image/')
    video = models.FileField(null=True,blank=True,upload_to='video/')
    date = models.DateField(auto_now=True)
    send_mail = models.BooleanField(default=False)

    def __str__(self):
      return self.title

class AcademicCalender(models.Model):
    year = models.DateField()
    whole_year_calender = models.FileField(null=True,blank=True,upload_to='calender/')
    sepcial_holidays = models.FileField(null=True,blank=True,upload_to='calender/')

    def __int__(self):
        return  self.year

class TimeTable(models.Model):
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='TimeTable')
    student_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='TimeTable')
    upload_timetable = models.ImageField(null=True,blank=True,upload_to='timetable/')


class Syllabus(models.Model):

  student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='Syllabus')
  upload_syllabus = models.ImageField(null=True,blank=True,upload_to='syllabus/')








