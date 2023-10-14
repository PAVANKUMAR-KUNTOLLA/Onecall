# from django.conf import settings
from rest_framework import serializers

from .models import *
from users.models import User

class TaxFilingSerializer(serializers.ModelSerializer):
    year = serializers.SerializerMethodField()

    class Meta:
        model = TaxFiling
        fields = ("id", "year", "service_type", "status")
        
    def get_year(self, instance):
        return instance.year.name
    
class FinancialYearSerializer(serializers.ModelSerializer):
    start_date = serializers.SerializerMethodField()
    end_date = serializers.SerializerMethodField()

    class Meta:
        model = FinancialYear
        fields = ("id", "name", "start_date", "end_date", "is_active")
        
    def get_start_date(self, instance):
        return instance.start_date.strftime("%Y-%m-%d")
    def get_end_date(self, instance):
        return instance.end_date.strftime("%Y-%m-%d")
