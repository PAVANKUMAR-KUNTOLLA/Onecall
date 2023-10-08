from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.validators import validate_email
from rest_framework import serializers
from users.models import User

class SignupSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    referralId = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def validate_email(self, email):
        is_valid_email = False
        try:
            validate_email(email)
        except Exception as excepted_message:
            raise Exception('Please use valid email for registration.')
            
        if User.objects.filter(email__iexact=email).exists():
            raise Exception('This user already exists. Please sign in.')
        return str(email).strip().lower()

    def save(self):
        name = self.validated_data['name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        referralId = self.validated_data['referralId']

        user = User.objects.create(name=name, email=email)
        user.is_active = True
        user.set_password(password)
        if referralId != None and  referralId != "" and "octs" in referralId and referralId.isalnum() and User.objects.filter(id=referralId.split("octs")[1]).exists() :
            user_referral = User.objects.get(id=referralId.split("octs")[1])
            user.referred_by = user_referral
        user.save()
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
    class Meta:
        model = User
        fields = ('id', 'name', 'email')