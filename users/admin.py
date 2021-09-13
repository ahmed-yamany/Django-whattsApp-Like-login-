from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FamTamUser


class AccountAdmin(UserAdmin):
    ordering = ('phone_number', )
    list_display = ('phone_number', 'date_joined', 'last_login',
                    'hide_phone', 'first_name', 'last_name',
                    'profile_image')
    search_fields = ('phone_number', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(FamTamUser, AccountAdmin)

