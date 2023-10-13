from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('app/home/', application),
    path('api/v1/tax_filing/', tax_filing),
    path('api/v1/personal_contact_details/', personal_contact_details),
    path('api/v1/spouse_details/', spouse_details),
    path('api/v1/dependant_details/', dependant_details),
    path('api/v1/bank_details/', bank_details),
    path('api/v1/income_details/', income_details),
    path('api/v1/confirm_details/', confirm_details),
    path('api/v1/choice_data/', choice_data),
]