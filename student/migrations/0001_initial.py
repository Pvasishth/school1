# Generated by Django 2.2 on 2019-05-11 11:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schoolclasses', '0001_initial'),
        ('account', '0001_initial'),
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
                ('address', models.CharField(blank=True, max_length=60, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message="PIN CODE must be entered in the format: '500072'. Up to 6 digits allowed", regex='^\\+?1?\\d{9,15}$')])),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.SchoolProfile')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_class', to='schoolclasses.Class')),
                ('student_section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_section', to='schoolclasses.Section')),
            ],
        ),
    ]
