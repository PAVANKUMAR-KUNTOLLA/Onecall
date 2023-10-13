from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(FinancialYear)
class FinancialYearAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'is_active', 'created_by']

@admin.register(TaxFiling)
class TaxFilingAdmin(admin.ModelAdmin):
    list_display = ['user', 'year', 'income',  'refund_type', 'bank', 'tax_docs', 'status', 'updated_at']

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ["filing", "updated_at", "created_at"]

@admin.register(Dependant)
class DependantAdmin(admin.ModelAdmin):
    list_display = ['filing', 'name', 'relationship', 'visa_type']

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['filing', 'name', 'ownership', 'created_at']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['filing', 'start_time', 'end_time', 'status']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['filing', 'amount', 'mode_of_payment', 'status']

@admin.register(Referal)
class ReferalAdmin(admin.ModelAdmin):
    list_display = ['referred_by', 'first_name', 'last_name', 'email', 'contact_no']