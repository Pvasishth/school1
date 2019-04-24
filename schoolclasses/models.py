from django.db import models

class Class(models.Model):
    class_name = models.CharField(max_length=150, null=True, blank=True)
    # section = models.ForeignKey(section, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name



class section(models.Model):
    section = models.CharField(max_length=50, help_text='Please Enter Number or alphabet')

    def __str__(self):
        return self.section





