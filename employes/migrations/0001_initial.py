# Generated by Django 2.2 on 2019-05-06 13:14

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schoolclasses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True)),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], max_length=10)),
                ('date_of_birth', models.DateField(max_length=8)),
                ('subject_expertise', multiselectfield.db.fields.MultiSelectField(choices=[('english', 'ENGLISH'), ('hindi', 'HINDI'), ('maths', 'MATHS'), ('science', 'SCIENCE'), ('social science', 'SOCIAL_SCIENCE')], max_length=42)),
                ('experience', models.PositiveSmallIntegerField()),
                ('joining_date', models.DateField(max_length=8)),
                ('email_id', models.EmailField(max_length=254)),
                ('highest_qualification', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework_title', models.CharField(max_length=255)),
                ('upload_homework', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Homework', to='schoolclasses.Class')),
                ('student_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Homework', to='schoolclasses.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_title', models.CharField(max_length=255)),
                ('upload_assignment', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Assignment', to='schoolclasses.Class')),
                ('student_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Assignment', to='schoolclasses.Section')),
                ('teacher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Assignment', to='employes.Teacher')),
            ],
        ),
    ]
