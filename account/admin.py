from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

class MediaUploadAdmin(admin.StackedInline):
        model = MediaUpload
        extra = 0

@admin.register(SchoolProfile)
class SchoolProfileAdmin(admin.ModelAdmin):
        list_display = ['__str__']
        inlines = [MediaUploadAdmin]

@admin.register(Alert)
class Alert(admin.ModelAdmin):
        list_display = ['__str__']

###########################################

# accounts.admin.py

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)



######################################################





admin.site.register(User,UserAdmin)
