# accounts.admin.py
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,Alert,AcademicCalender,TimeTable,Syllabus


admin.site.register(User)
admin.site.register(Alert)
admin.site.register(AcademicCalender)
admin.site.register(TimeTable)
admin.site.register(Syllabus)
admin.site.unregister(Group)