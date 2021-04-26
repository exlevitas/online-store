from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.

class CustomersAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'name', 'rassilka']
admin.site.register(Customers, CustomersAdmin)

class CustomUserAdmin(UserAdmin):
    pass
admin.site.register(CustomUser, CustomUserAdmin)
