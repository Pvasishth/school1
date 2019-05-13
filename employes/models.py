from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from django.conf import settings

user = settings.AUTH_USER_MODEL
from schoolclasses.models import *
from ckeditor_uploader.fields import  RichTextUploadingField
from django.urls import reverse
from datetime import datetime
from account.models import SchoolProfile


class Teacher(models.Model):

  school = models.ForeignKey(SchoolProfile, on_delete=models.DO_NOTHING)
  GENDER_CHOICES  = (('male','MALE'),('female','FEMALE'))
  SUBJECT_CHOICES = (('english','ENGLISH'),('hindi','HINDI'),('maths','MATHS'),('science','SCIENCE'),
                    ('social science','SOCIAL_SCIENCE'))
  CLASSES_CHOICES = (('nur', 'NUR'),('lkg','LKG'),('ukg','UKG'),('1st','1ST'),('2nd','2nd'),('3rd','3rd'),('4th','4th'),('5th','5th'),('6th','6th'),('7th','7th'),
                    ('8th','8th'),('9th','9th'),('10th','10th'),('11th','11th'),('12th','12th'))


  full_name = models.CharField(max_length=20)
  user = models.OneToOneField(user,on_delete=models.CASCADE,null=True,blank=True,related_name='teacher_profile')
  age = models.PositiveSmallIntegerField()
  gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
  date_of_birth = models.DateField(max_length=8,blank=True,null=True)
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




class Homework(models.Model):
  school = models.ForeignKey(SchoolProfile, on_delete=models.DO_NOTHING)
  student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='homework')
  student_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='homework')
  teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='homework')
  homework_title = models.CharField(max_length=255)
  upload_homework = RichTextUploadingField(null=True, blank=True)
  upload_file = models.FileField(null=True, blank=True)
  def __str__(self):
    return self.homework_title
  def get_absolute_url(self):
    return f"/homework/{self.id}/"


class Assignment(models.Model):
  school = models.ForeignKey(SchoolProfile, on_delete=models.DO_NOTHING)
  student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='assignment')
  student_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='assignment')
  teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='assignment')
  assignment_title = models.CharField(max_length=255)
  upload_assignment = RichTextUploadingField(null=True, blank=True)
  upload_file = models.FileField(null=True, blank=True)
  def __str__(self):
    return self.assignment_title




class Gallery(models.Model):
  school = models.ForeignKey(SchoolProfile, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200, null=True, blank=True)
  description = models.TextField(blank=True)
  photo_1 = models.ImageField(blank=True)
  photo_2 = models.ImageField(blank=True)
  photo_3 = models.ImageField(blank=True)
  photo_4 = models.ImageField(blank=True)
  photo_5 = models.ImageField(blank=True)
  photo_6 = models.ImageField(blank=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title