from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Prac)
class Prac_Admin(admin.ModelAdmin):
    fieldsets = (
        ("basic", {"fields": ("title", "video", "score")},),
        # ("times", {"fields": ("created", "updated")}),
    )
