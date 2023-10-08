from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'referred_by', 'referral_id']
    search_fields = ['name', 'email']
    list_filter = ['is_active']