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
