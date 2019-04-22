from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField

#####################################################
from django.contrib.auth.models import AbstractUser
#from django.utils.html import escape, mark_safe

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_principal = models.BooleanField(default=False)

#####################################################

class SchoolProfile(models.Model):
  principal = models.OneToOneField(User,on_delete = models.CASCADE, related_name = 'schoolprofile')
  school_name = models.CharField(max_length = 20 , null =True ,blank = True)
  username = models.CharField(max_length=25, unique=True, default='')
  password = models.CharField(max_length=30, default='')
  #address for the school
  state = models.CharField(max_length = 20, null =True ,blank = True)
  city = models.CharField(max_length = 20 , null =True ,blank = True)
  area = models.CharField(max_length = 20 , null =True ,blank = True)
  pincode = models.PositiveIntegerField(null = True , blank = True ,default = '1')
  landmark = models.CharField(max_length = 20 , null =True ,blank = True)

  #phone number field
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '8885559997'. Up to 12 digits allowed along with country code.")
  phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True , null = True)

  #school website
  website = models.URLField(null = True , blank = True)

#for uploading the media by the school 

class MediaUpload(models.Model):
  SchoolProfile = models.ForeignKey(SchoolProfile,on_delete = models.CASCADE, related_name = 'MediaUpload')
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
  title = models.CharField(max_length=50, default=True)
  message = models.TextField(default=True)
  image = models.ImageField(null=True,blank=True)
  video = models.FileField(null=True,blank=True)
  date = models.DateField(auto_now=True)


  def __str__(self):
    return self.title

class Teacher(models.Model):


  GENDER_CHOICES=(('male','MALE'),('female','FEMALE'))
  SUBJECT_CHOICES=(('english','ENGLISH'),('hindi','HINDI'),('maths','MATHS'),('science','SCIENCE'),
                   ('social science','SOCIAL_SCIENCE'))
  CLASSES_CHOICES = (('nur','NUR'),('lkg','LKG'),('ukg','UKG'),('1st','1ST'),('2nd','2nd'),('3rd','3rd'),('4th','4th'),('5th','5th'),('6th','6th'),('7th','7th'),
                     ('8th','8th'),('9th','9th'),('10th','10th'),('11th','11th'),('12th','12th'))

  name = models.CharField(max_length=20,null=True,blank=True)
  age = models.PositiveSmallIntegerField(null = True,blank=True)
  gender = models.CharField(max_length=10,choices=GENDER_CHOICES,default='none')
  date_of_birth = models.DateField(null=True,blank=True)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '8885559997'. Up to 12 digits allowed along with country code.")
  mobile_number = models.CharField(validators=[phone_regex], max_length=12, blank=True , null = True)
  subject_expertise =MultiSelectField(choices=SUBJECT_CHOICES,null=True,blank=True)
  experience = models.PositiveSmallIntegerField(null = True,blank=True)
  joining_date = models.DateField(null = True,blank=True)
  email_id = models.EmailField(null = True,blank=True)
  classes_alloted = MultiSelectField(choices=CLASSES_CHOICES,null=True,blank=True)
  highest_qualification = models.CharField(max_length=20,null=True,blank=True)