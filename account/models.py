from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from django.utils import timezone
from django.contrib.auth.models import (
  AbstractUser,
AbstractBaseUser,
BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None,is_admin=False,is_active=True,is_staff=False):
      if not email:
        raise ValueError('User must have Email id')

      user_obj = self.model(
        email=self.normalize_email(email),
      )
      user_obj.admin=is_admin
      user_obj.staff=is_staff
      user_obj.is_active=is_active
      user_obj.set_password(password)
      user_obj.save(using=self._db)
      return user_obj

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user_obj = self.create_user(
            email,
            password=password,
        )
        user_obj.staff = True
        user_obj.admin = True
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user_obj = self.create_user(
            email,
            password=password,
        )
        user_obj.admin= True
        user_obj.save(using=self._db)
        return user_obj

    def create_principal(self, email,password):
      user_obj = self.create_user(
        email,
        password=password,
      )
      user_obj.principal = True
      user_obj.save(using=self._db)
      return user_obj



    def create_teacher(self, email, password=None):
        user_obj = self.create_user(
            email,
            password=password,
        )
        user_obj.teacher = True
        user_obj.save(using=self._db)
        return user_obj


    def create_student(self, email,password=None):
        user_obj = self.create_user(
            email,
            password=password,
        )
        user_obj.student = True
        user_obj.save(using=self._db)
        return user_obj




class User(AbstractBaseUser):
    email = models.EmailField(
      verbose_name='email address',
      max_length=255,
      unique=True
    )
    bio =models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    student = models.BooleanField(default=False,
                                     help_text=(
                                         'For Students Permissions'

                                     ),
                                     )

    teacher = models.BooleanField(default=False,
                                     help_text=(
                                         'For Teachers Permissions'

                                     ),)
    principal = models.BooleanField(default=False,
                                       help_text=(
                                          'For Principal permissions'
                                       ),
                                       )

    objects = UserManager()

    EMAIL_FIELD = 'email'
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
    def is_staff(self):
      "Is the user a member of staff?"
      return self.staff

    @property
    def is_admin(self):
      "Is the user a admin member?"
      return self.admin

    @property
    def is_principal(self):
      return self.principal

    @property
    def active(self):
      "Is the user active?"
      return self.is_active

    @property
    def is_teacher(self):
        return self.teacher

    @property
    def is_student(self):
        return self.student







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
  image = models.ImageField(null=True,blank=True)
  video = models.FileField(null=True,blank=True)
  date = models.DateField(auto_now=True)




  def __str__(self):
    return self.title


