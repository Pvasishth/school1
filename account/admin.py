# accounts.admin.py
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


admin.site.register(User)



# Remove Group Model from admin. We're not using it.

admin.site.register(User, UserAdmin)
admin.site.register(Alert)
admin.site.register(AcademicCalender)
admin.site.register(TimeTable)
admin.site.register(Syllabus)
admin.site.unregister(Group)