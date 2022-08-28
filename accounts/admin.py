from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from.models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email','is_staff','is_superuser']
    search_fields = ['email','username']
    readonly_fields = ['id', 'date_joined','last_login']



admin.site.register(CustomUser,CustomUserAdmin)
