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

class AppointmentSerializer(serializers.ModelSerializer):
    filing = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ("id", "filing", "date", "start_time", "end_time", "status")
    
    def get_filing(self, instance):
        return instance.filing.user.email
    def get_date(self, instance):
        return instance.start_time.strftime("%d %b %Y")
    def get_start_time(self, instance):
        return instance.start_time.strftime("%H:%M:%S")
    def get_end_time(self, instance):
        return instance.end_time.strftime("%H:%M:%S")

class ReferalSerializer(serializers.ModelSerializer):
    referred_by = serializers.SerializerMethodField()
    class Meta:
        model = Referal
        fields = ('id', 'first_name', "last_name", 'email', "contact_no",  "referred_by")

    def get_referred_by(self, instance):
        if instance.referred_by:
            return instance.referred_by.email
        else:
            return ""
   