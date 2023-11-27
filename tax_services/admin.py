from django.contrib import admin
from .models import *

from django.contrib.auth.models import Group

admin.site.unregister(Group)

try:
    from rest_framework.authtoken.models import TokenProxy as DRFToken
except ImportError:
    from rest_framework.authtoken.models import Token as DRFToken

admin.site.unregister(DRFToken)


# Register your models here.
@admin.register(FinancialYear)
class FinancialYearAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'is_active', 'created_by']

@admin.register(TaxFiling)
class TaxFilingAdmin(admin.ModelAdmin):
    list_display = ['user', 'year', 'income',  'refund_type', 'bank', 'status', 'updated_at']

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ["filing", "updated_at", "created_at"]

@admin.register(OtherIncome)
class OtherIncomeAdmin(admin.ModelAdmin):
    list_display = ["filing", "income_description", "income_amount", "updated_at", "created_at"]

@admin.register(Dependant)
class DependantAdmin(admin.ModelAdmin):
    list_display = ['filing', 'name', 'relationship', 'visa_type']

@admin.register(TaxDocs)
class TaxDocsAdmin(admin.ModelAdmin):
    list_display = ['filing', 'file_name', 'created_at', 'updated_at']

@admin.register(TaxReturns)
class TaxReturnsAdmin(admin.ModelAdmin):
    list_display = ['filing', 'file_name', 'created_at', 'updated_at']

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['filing', 'name', 'ownership', 'created_at']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['filing', 'start_time', 'end_time', 'status']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['filing', 'amount', 'mode_of_payment', 'status']

@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ['filing', 'service_type', 'refund_type', 'standard_refund', 'standard_fee', 'itemized_refund', 'itemized_fee', 'discount', 'paid_advance', 'max_itemized_refund', 'max_itemized_fee']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['filing', 'message', 'by']

@admin.register(Referal)
class ReferalAdmin(admin.ModelAdmin):
    list_display = ['referred_by', 'first_name', 'last_name', 'email', 'contact_no']