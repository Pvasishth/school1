# Generated by Django 2.1.8 on 2019-05-13 10:00

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schoolclasses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_title', models.CharField(max_length=255)),
                ('upload_assignment', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Assignment', to='schoolclasses.Class')),
                ('student_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Assignment', to='schoolclasses.Section')),
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
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], max_length=10)),
                ('date_of_birth', models.DateField(blank=True, max_length=8, null=True)),
                ('subject_expertise', multiselectfield.db.fields.MultiSelectField(choices=[('english', 'ENGLISH'), ('hindi', 'HINDI'), ('maths', 'MATHS'), ('science', 'SCIENCE'), ('social science', 'SOCIAL_SCIENCE')], max_length=42)),
                ('experience', models.PositiveSmallIntegerField()),
                ('joining_date', models.DateField(blank=True, max_length=8, null=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('highest_qualification', models.CharField(max_length=20)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='teacher_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Assignment', to='employes.Teacher'),
        ),
    ]
