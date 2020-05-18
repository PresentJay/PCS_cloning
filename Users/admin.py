from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(models.User)
class UserAdmin(UserAdmin):

    fieldsets = (("Custom Profile", {"fields": ["user_birth"]}),)

    list_display = (
        "username",
        "is_staff",
        "is_superuser",
    )
