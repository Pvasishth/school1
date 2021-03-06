# Generated by Django 2.1.8 on 2019-05-13 10:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schoolclasses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=20)),
                ('student_roll_number', models.PositiveIntegerField()),
                ('student_reg_number', models.CharField(max_length=20)),
                ('student_previous_school', models.CharField(max_length=20)),
                ('student_previous_school_transfer_certificate', models.ImageField(blank=True, null=True, upload_to='')),
                ('father_name', models.CharField(max_length=20)),
                ('mother_name', models.CharField(max_length=20)),
                ('guardian_mobile_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '8885559997'. Up to 12 digits allowed along with country code.", regex='^\\+?1?\\d{9,15}$')])),
                ('parents_email_id', models.EmailField(max_length=254)),
                ('student_email_id', models.EmailField(max_length=254)),
                ('family_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_of_birth', models.DateField()),
                ('home_address', models.CharField(blank=True, max_length=60, null=True)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_class', to='schoolclasses.Class')),
                ('student_section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_section', to='schoolclasses.Section')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
