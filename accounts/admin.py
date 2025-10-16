from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
     list_display = ('username', 'email', 'role', 'is_active', 'is_staff', 'date_joined')
     list_filter = ('role', 'is_active', 'is_staff')
     search_fields = ('username', 'email')
     ordering = ('-date_joined',)

     fieldsets = ( (None, {'fields': ('username', 'email', 'password', 'role', 'contact_info')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
     add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'is_active', 'is_staff')}
        ),
    )
     

     