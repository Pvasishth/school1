# Generated by Django 2.2 on 2019-04-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190422_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='family_photo',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]
