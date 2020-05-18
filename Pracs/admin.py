from django.contrib import admin
from . import models

# Register your models here.


@admin.site.register(models.Prac)
class PracAdmin(admin.ModelAdmin):
    fieldsets = (
        ("basic", {"fields": ("title", "video", "score")},),
        ("times", {"fields": ("created", "updated")}),
    )
