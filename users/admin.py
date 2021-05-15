from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # fields to be displayed on admin site for user creation and user change
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "classes": ("wide",),
            'fields': ('age',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "classes": ("wide",),
            "fields": ('age',)}),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)
