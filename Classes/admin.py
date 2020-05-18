from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Class)
class Class_Admin(admin.ModelAdmin):
    fieldsets = (("basic", {"fields": ("title", "video", "thumbnail", "level"),}),)

