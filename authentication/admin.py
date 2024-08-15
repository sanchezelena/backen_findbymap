from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('rol', 'is_admin', 'is_employee')}),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_employee', 'is_admin')

admin.site.register(User, CustomUserAdmin)
