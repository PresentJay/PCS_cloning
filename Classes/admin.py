from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    fieldsets = (("basic", {"fields": ("title", "video", "thumbnail", "level"),}),)

