from django.contrib import admin
from .models import StudentProfile

# Register your models here.
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
        list_display = ['__str__']
