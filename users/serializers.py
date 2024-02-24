from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.validators import validate_email
from rest_framework import serializers
from users.models import User, Associate
from tax_services.models import TaxFiling, Appointment
from datetime import datetime

class SignupSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    firstName = serializers.CharField(required=True)
    lastName = serializers.CharField(required=True)
    gender = serializers.CharField(required=False)
    role = serializers.CharField(required=True)
    referralId = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    contact = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    associateCode = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    uploadDocsView = serializers.BooleanField(required=False)
    manageAppointment = serializers.BooleanField(required=False)

    def validate_email(self, email):
        is_valid_email = False
        try:
            validate_email(email)
        except Exception as excepted_message:
            raise Exception('Please use valid email for registration.')
            
        if User.objects.filter(email__iexact=email).exists() and not self.initial_data.get("role") == "ADMIN":
            raise Exception('This user already exists. Please sign in.')
        return str(email).strip().lower()

    def validate_role(self, role):
        if role == "ADMIN":
            contact = self.initial_data.get("contact")
            associateCode = self.initial_data.get("associateCode")
            uploadDocsView = self.initial_data.get("uploadDocsView")
            manageAppointment = self.initial_data.get("manageAppointment")

            if not contact:
                raise serializers.ValidationError('Contact No is required for admin users.')

            if not associateCode:
                raise serializers.ValidationError('Associate code is required for admin users.')
            else:
                if Associate.objects.filter(code__iexact=self.initial_data.get("associateCode")).exists():
                    raise Exception('User with this Associate code already exists. Please sign in.')

            if not uploadDocsView:
                raise serializers.ValidationError('Upload docs view is required for admin users.')

            if not manageAppointment:
                raise serializers.ValidationError('Manage appointment is required for admin users.')

        return role

    def save(self):
        first_name = self.validated_data['firstName']
        last_name = self.validated_data['lastName']
        if "gender" in self.validated_data:
            gender = self.validated_data['gender']
        else:
            gender = "MALE"
        email = self.validated_data['email']
        password = self.validated_data['password']
        role = self.validated_data["role"]
        if role == "CLIENT":
            referralId = self.validated_data['referralId']
        else:
            referralId = None

        if not User.objects.filter(email__iexact=email).exists():
            user = User.objects.create(first_name=first_name,last_name=last_name,gender=gender,email=email,role=role)
            user.is_active = True
            user.set_password(password)
            if referralId != None and  referralId != "" and "octs" in referralId and referralId.isalnum() and User.objects.filter(id=referralId.split("octs")[1]).exists() :
                user_referral = User.objects.get(id=referralId.split("octs")[1])
                user.referred_by = user_referral
            user.save()
        else:
            user = User.objects.get(email=email)

        if user.role == "ADMIN":
            associate = Associate.objects.create(user=user, code=self.validated_data["associateCode"], 
                    upload_docs_view=self.validated_data["uploadDocsView"], manage_appointment=self.validated_data["manageAppointment"], 
                    contact_no=self.validated_data["contact"])
            associate.save()
        return user

class AuthenticationSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']
        if email and password:
            user = authenticate(request=self.context['request'], email=str(email).strip().lower(), password=password)
            print(user)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')

            if not user.is_active:
                msg = _('User is set Not Active')
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs

class UserProfileSerializer(serializers.ModelSerializer):
    phone_no = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    referred_by = serializers.SerializerMethodField()
    referral_id = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'first_name', "last_name", "gender", 'email', "role", "phone_no", "address", "referred_by", "referral_id")
        
    def get_role(self, instance):
        if instance.role:
            return instance.role
        else:
            return "CLIENT"
        
    def get_phone_no(self, instance):
        if instance.contact:
            return instance.contact.primary_number
        else:
            return ""
    def get_address(self, instance):
        if instance.contact:
            return instance.contact.street
        else:
            return ""
    def get_referred_by(self, instance):
        if instance.referred_by:
            return instance.referred_by.email
        else:
            return ""
    def get_referral_id(self, instance):
        if instance.referred_by:
            return instance.referred_by.referral_id
        else:
            return ""

class UserTaxFilingSerializer(serializers.ModelSerializer):
    phone_no = serializers.SerializerMethodField()
    filing = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'first_name', "last_name", 'email', "phone_no", "filing")
        
    def get_phone_no(self, instance):
        if instance.contact:
            return instance.contact.primary_number
        else:
            return ""

    def get_filing(self, instance):
        if TaxFiling.objects.filter(user__id=instance.id).exists():
            if Appointment.objects.filter(filing__user__id=instance.id, status="BOOKED").exists():
                appointments = Appointment.objects.filter(filing__user__id=instance.id, status="BOOKED").order_by("-created_at")
                for appointment_ins in appointments:
                    return {"taxFilingId":appointment_ins.filing.id, "taxFilingYear":appointment_ins.filing.year.name, "appointmentId":appointment_ins.id, "appointmentDate":datetime.strftime(appointment_ins.start_time, "%d %b %Y"), "appointmentTime":datetime.strftime(appointment_ins.start_time, "%H:%M")}
            else:
                tax_filings = TaxFiling.objects.filter(user__id=instance.id).order_by("-created_at")
                for tax_filing_ins in tax_filings:
                    return {"taxFilingId":tax_filing_ins.id, "taxFilingYear":tax_filing_ins.year.name, "appointmentId":"", "appointmentDate":"", "appointmentTime":""}      

        else:
            return {"taxFilingId":"", "taxFilingYear":"", "appointmentId":"", "appointmentDate":"", "appointmentTime":""}      

class AssociateSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = Associate
        fields = ('id', 'first_name', "last_name", 'email', "role", "contact_no", "code", "upload_docs_view", "manage_appointment" )
        
    def get_first_name(self, instance):
        if instance.user:
            return instance.user.first_name
        else:
            return ""
    
    def get_last_name(self, instance):
        if instance.user:
            return instance.user.last_name
        else:
            return ""

    def get_email(self, instance):
        if instance.user:
            return instance.user.email
        else:
            return ""
    
    def get_role(self, instance):
        if instance.user:
            return instance.user.role
        else:
            return ""

