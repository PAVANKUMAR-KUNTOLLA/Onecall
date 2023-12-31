from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('app/home/', application),
    path('api/v1/tax_filing/', tax_filing),
    path('api/v1/personal_contact_details/', personal_contact_details),
    path('api/v1/spouse_details/', spouse_details),
    path('api/v1/dependant_details/', dependant_details),
    path('api/v1/delete_dependant/', delete_dependant),
    path('api/v1/bank_details/', bank_details),
    path('api/v1/income_details/', income_details),
    path('api/v1/upload_tax_docs/', upload_tax_docs),
    path('api/v1/confirm_details/', confirm_details),
    path('api/v1/choice_data/', choice_data),
    path('api/v1/tax_years/', tax_years),
    path('api/v1/my_services/', my_services),
    path('api/v1/download_tax_docs/',download_tax_docs),
    path('api/v1/delete_tax_docs/',delete_tax_docs),
    path('api/v1/book_appointment/', book_appointment),
    path('api/v1/appointment_details/', appointment_details),
    path('api/v1/delete_appointment/', delete_appointment),
    path('api/v1/make_referal/',make_referal),
    path('api/v1/referal_details/', referal_details),
    path('api/v1/download_template',download_template),
]