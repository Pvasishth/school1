# Generated by Django 2.1.8 on 2019-05-13 10:00

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schoolclasses', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_principal', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AcademicCalender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('whole_year_calender', models.FileField(blank=True, null=True, upload_to='calender/')),
                ('sepcial_holidays', models.FileField(blank=True, null=True, upload_to='calender/')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='alert_image/')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default=True, max_length=50)),
                ('Message', models.TextField(default=True)),
                ('Date', models.DateField(default=django.utils.timezone.now)),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='')),
                ('video1', models.URLField(blank=True, null=True)),
                ('video2', models.URLField(blank=True, null=True)),
                ('school_brouche', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('pincode', models.PositiveIntegerField(null=True)),
                ('landmark', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '88855599test@gmail.com97'. Up to 12 digits allowed along with country code.", regex='^\\+?1?\\d{9,15}$')])),
                ('website', models.URLField(blank=True, null=True)),
                ('principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schoolprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_syllabus', models.ImageField(blank=True, null=True, upload_to='syllabus/')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Syllabus', to='schoolclasses.Class')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_timetable', models.ImageField(blank=True, null=True, upload_to='timetable/')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TimeTable', to='schoolclasses.Class')),
                ('student_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TimeTable', to='schoolclasses.Section')),
            ],
        ),
        migrations.AddField(
            model_name='mediaupload',
            name='SchoolProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MediaUpload', to='account.SchoolProfile'),
        ),
    ]