from django.contrib import admin

from .models import SchoolProfile,MediaUpload

class MediaUploadAdmin(admin.StackedInline):
        model = MediaUpload
        extra = 0

@admin.register(SchoolProfile)
class SchoolProfileAdmin(admin.ModelAdmin):
        list_display = ['__str__']
        inlines = [MediaUploadAdmin]