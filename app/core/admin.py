"""Django admin customization"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from core import models

class UserAdmin(BaseAdmin):
    """Define the admin page for users"""
    ordering = ['id']
    list_display = ['email', 'name']

admin.site.register(models.User, UserAdmin)