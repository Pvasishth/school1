from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

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
  Title = models.CharField(max_length=50, default=True)
  Message = models.TextField(default=True)
  Date = models.DateField(auto_now=True)


  def __str__(self):
    return self.Title