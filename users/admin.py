from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'referred_by', 'referral_id']
    search_fields = ['email']
    list_filter = ['is_active']
    readonly_fields =  ['name', 'email', 'referred_by', 'referral_id', 'status', 'dob', 'first_name', 'last_name', 'middle_name', 'job_title', 'residential_status', 'gender']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'state', 'country', 'primary_number_country_code', 'primary_number',]
    readonly_fields =  ['user', 'city', 'state', 'country', 'primary_number_country_code', 'primary_number',]