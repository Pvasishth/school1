from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField
from multiselectfield import MultiSelectField
from django.core.validators import RegexValidator
from account.models import SchoolProfile



class Class(models.Model):
    school = models.ForeignKey(SchoolProfile, on_delete=models.DO_NOTHING)
    subjects = (('Hindi', 'Hindi'),
                ('English', 'English'),
                ('Mathematics', 'Mathematics'),
                ('Science', 'Science'),
                ('Social_Studies', 'Social_Studies'))

    class_name = models.CharField(max_length=150, null=True, blank=True)
    select_subjects = MultiSelectField(choices=subjects, max_choices=3)
    content = RichTextUploadingField(null=True, blank=True)


    def __str__(self):
        return self.class_name



class Section(models.Model):
    student_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    section = models.CharField(max_length=50, help_text='Please Enter Number or alphabet')

    def __str__(self):
        return self.student_section



