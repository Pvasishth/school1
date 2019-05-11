# Generated by Django 2.2 on 2019-05-11 11:07

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_title', models.CharField(max_length=255)),
                ('upload_assignment', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True)),
                ('photo_1', models.ImageField(blank=True, upload_to='')),
                ('photo_2', models.ImageField(blank=True, upload_to='')),
                ('photo_3', models.ImageField(blank=True, upload_to='')),
                ('photo_4', models.ImageField(blank=True, upload_to='')),
                ('photo_5', models.ImageField(blank=True, upload_to='')),
                ('photo_6', models.ImageField(blank=True, upload_to='')),
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
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.SchoolProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework_title', models.CharField(max_length=255)),
                ('upload_homework', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.SchoolProfile')),
            ],
        ),
    ]