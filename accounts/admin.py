from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ['email',  'date_joined',  'last_login', 'first_name', 'last_name', 'is_active']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email','username', 'password')}),  # Include 'password' field
        ('Personal Information', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin' ,'is_superadmin')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('date_joined', 'last_login')

admin.site.register(Account, AccountAdmin)