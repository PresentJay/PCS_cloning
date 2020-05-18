from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

# admin.site.register(models.User, UserAdmin)
@admin.register(models.User)
class User_Admin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (("Custom Profile", {"fields": ["birthday"]}),)

    list_display = (
        "username",
        "is_staff",
        "is_superuser",
    )
