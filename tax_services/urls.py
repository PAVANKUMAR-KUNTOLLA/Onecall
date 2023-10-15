from django.urls import path
from .views import *

urlpatterns = [
    # path('', index),
    path('', application),
    path('api/v1/tax_filing/', tax_filing),
    path('api/v1/personal_contact_details/', personal_contact_details),
    path('api/v1/spouse_details/', spouse_details),
    path('api/v1/dependant_details/', dependant_details),
    path('api/v1/bank_details/', bank_details),
    path('api/v1/income_details/', income_details),
    path('api/v1/upload_tax_docs/', upload_tax_docs),
    path('api/v1/confirm_details/', confirm_details),
    path('api/v1/choice_data/', choice_data),
    path('api/v1/tax_years/', tax_years),
    path('api/v1/my_services/', my_services),
    path('api/v1/download_tax_docs/',download_tax_docs),
    path('api/v1/delete_tax_docs/',delete_tax_docs),

]