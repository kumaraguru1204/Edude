from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StudentProfile

admin.site.register(StudentProfile)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'full_name', 'role', 'email', 'is_active', 'is_staff')
    
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    
    search_fields = ('username', 'full_name', 'email')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'email')}),
        ('Role & Permissions', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'email', 'role', 'password1', 'password2'),
        }),
    )