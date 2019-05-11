# Generated by Django 2.2 on 2019-05-07 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolclasses', '0001_initial'),
        ('account', '0003_timetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_syllabus', models.FileField(blank=True, null=True, upload_to='')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Syllabus', to='schoolclasses.Class')),
            ],
        ),
    ]
