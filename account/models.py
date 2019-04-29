from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from django.utils import timezone
from django.contrib.auth.models import (
  AbstractUser,
BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None,is_admin=False,is_active=True,is_staff=False):
      if not email:
        raise ValueError('User must have Email id')

      user = self.model(
        email=self.normalize_email(email),
      )
      user.is_superuser=is_admin
      user.is_staff=is_staff
      user.is_active=is_active
      user.set_password(password)
      user.save(using=self._db)
      return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff= True
        user.save(using=self._db)
        return user

    def create_principal(self, email,password):
      user = self.create_user(
        email,
        password=password,
      )
      user.is_principal = True
      user.save(using=self._db)
      return user



    def create_teacher(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_teacher = True
        user.save(using=self._db)
        return user


    def create_student(self, email,password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_student = True
        user.save(using=self._db)
        return user




class user(AbstractUser):
    email = models.EmailField(
      verbose_name='email address',
      max_length=255,
      unique=True
    )
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_principal = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
      return self.email


    def get_short_name(self):
      return self.email

    def __str__(self):
      return self.email

    def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return True

    def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

    @property
    def staff(self):
      "Is the user a member of staff?"
      return self.is_staff

    @property
    def admin(self):
      "Is the user a admin member?"
      return self.is_superuser

    # @property
    # def is_principal(self):
    #   return self.is_principal

    @property
    def active(self):
      "Is the user active?"
      return self.is_active











class SchoolProfile(models.Model):
  principal = models.OneToOneField(user,on_delete = models.CASCADE, related_name = 'schoolprofile')
  school_name = models.CharField(max_length = 20)
  username = models.CharField(max_length=25, unique=True)
  password = models.CharField(max_length=30)
  #address for the school
  state = models.CharField(max_length = 20)
  city = models.CharField(max_length = 20)
  area = models.CharField(max_length = 20)
  pincode = models.PositiveIntegerField()
  landmark = models.CharField(max_length = 20)

  #phone number field
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '8885559997'. Up to 12 digits allowed along with country code.")
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
  image = models.ImageField(null=True,blank=True)
  video = models.FileField(null=True,blank=True)
  date = models.DateField(auto_now=True)




  def __str__(self):
    return self.title


