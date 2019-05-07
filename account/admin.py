# accounts.admin.py
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import *
from .models import User,AcademicCalender,Alert,TimeTable

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'admin','principal','teacher','student')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('bio','avatar',)}),
        ('Permissions', {'fields': ('admin','staff','principal','teacher','student')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','avatar','bio','admin','staff','principal','teacher','student')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Alert)
admin.site.register(AcademicCalender)
admin.site.register(TimeTable)
admin.site.register(Syllabus)
admin.site.unregister(Group)

