import os
import io
import re
import copy
import datetime

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import *
from django.core.mail import EmailMessage
from onecall.settings import DEFAULT_FROM_EMAIL
from rest_framework.authtoken.models import Token

# reset password imports
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

# Create your views here.

@api_view(['POST'])
def signup(request):
    try:
        if request.method == "POST":
            data = request.data.copy()
            signup_serializer = SignupSerializer(
                data=data, context={'request': request})
            signup_serializer.is_valid(raise_exception=True)

            if data["role"] == "ADMIN" and not request.user.is_superuser:
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)

            if data["role"] == "CLIENT" and data["passwordConfirmation"] != data["password"]:
                context = None
                status_flag = False
                message = "Password mismatch"
                status_code = status.HTTP_406_NOT_ACCEPTABLE
                context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
                return Response(status=status_code, data= context)

            # print(data)
            signup_serializer = SignupSerializer(
                data=data, context={'request': request})
            signup_serializer.is_valid(raise_exception=True)
            print(signup_serializer.data)
            signup_serializer.save()
            user_data = signup_serializer.data

            if user_data["role"] == "CLIENT":
                subject = 'User Signed Up - Onecall Tax Services'
                login_url = request.build_absolute_uri(f'/login')
                message = f'"This is an Automated Mail" \n\nHi {user_data["email"]}, \nYou have successfully signed-up for a user account, for the Onecall Tax Services. You can login now.\n\nregards,\nOnecall Tax Services Digitisation Team. \n\n you can login through the below link - {login_url}'
                
                from_email = DEFAULT_FROM_EMAIL
                to = [user_data["email"], ]
                email = EmailMessage(subject, message, from_email, to)
                email.send()

            context = None
            status_flag = True
            message = "Success"
            status_code = status.HTTP_200_OK
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)

        else:
            context = None
            status_flag = False
            message = "Only Post Method available"
            status_code = status.HTTP_405_METHOD_NOT_ALLOWED
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)

    except Exception as excepted_message:
        print(excepted_message)
        context = None
        status_flag = False
        message = str(excepted_message)
        status_code = status.HTTP_400_BAD_REQUEST
        context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
        return Response(status=status_code, data= context)

@api_view(['POST'])
def login(request):
    data = request.data.copy()
    login_serializer = AuthenticationSerializer(
        data=data, context={'request': request})
    login_serializer.is_valid(raise_exception=True)
    user = login_serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    data = {
        'token': token.key
    }
    context = data
    status_flag = True
    message = None
    status_code = status.HTTP_200_OK
    context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
    return Response(status=status_code, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    print(request.user)
    try:
        token = Token.objects.get(user=request.user)
    except Token.DoesNotExist:
        token = None

    if token:
        token.delete()
    
    context = None
    status_flag = False
    message = None
    status_code = status.HTTP_204_NO_CONTENT
    context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
    return Response(status=status_code, data= context)

@api_view(['GET', ])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    try:
        user = request.user
        if request.method == 'GET':
            profile_data = UserProfileSerializer(instance=user).data

            context = profile_data
            status_flag = True
            message = None
            status_code = status.HTTP_200_OK
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)

        else:
            context = None
            status_flag = False
            message = "Only Get Method available"
            status_code = status.HTTP_405_METHOD_NOT_ALLOWED
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)

    except Exception as excepted_message:
        print(excepted_message)
        context = None
        status_flag = False
        message = str(excepted_message)
        status_code = status.HTTP_400_BAD_REQUEST
        context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
        return Response(status=status_code, data= context)

@api_view(['POST'])
def forgot_password(request):
    data = request.data.copy()
    try:
        if User.objects.filter(email=data['email']).exists():
            user = User.objects.get(email=data['email'])
            if not user.is_active:
                context = None
                status_flag = False
                message = 'User is set Not Active'
                status_code = status.HTTP_400_BAD_REQUEST
                context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
                return Response(status=status_code, data= context)
                                                
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)               
            # reset_password_url = f'{get_current_site(request=request).domain}/reset-password/{uidb64}/{token}'        
            reset_password_url = request.build_absolute_uri(f'/reset-password/{uidb64}/{token}')  

            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                    reset_password_url

            subject = "Reset your passsword"            
            from_email = DEFAULT_FROM_EMAIL
            to = [data["email"], ]
            email = EmailMessage(subject, email_body, from_email, to)
            email.send()

            context = None
            status_flag = True
            message = 'We have sent reset code. Please check your email'
            status_code = status.HTTP_200_OK
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)
        
        else:
            context =  None
            status_flag = False
            message = "User not found. Not a valid email"
            status_code = status.HTTP_404_NOT_FOUND
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)

    except Exception as excepted_message:
        print(excepted_message)
        context = None
        status_flag = False
        message = "Password Reset Failed"
        status_code = status.HTTP_400_BAD_REQUEST
        context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
        return Response(status=status_code, data= context)



@api_view(['POST'])
def reset_password(request):
    data = request.data.copy()
    try:
        id = smart_str(urlsafe_base64_decode(data["uidb64"]))
        user = User.objects.get(id=id)

        if not PasswordResetTokenGenerator().check_token(user, data["token"]):
            context = None
            status_flag = False
            message = "Reset token expired, please request a new one"
            status_code = status.HTTP_400_BAD_REQUEST
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)

        user.set_password(data["password"])
        user.save()

        context = None
        status_flag = True
        message = 'Password reset success'
        status_code = status.HTTP_200_OK
        context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
        return Response(status=status_code, data= context)

    except Exception as excepted_message:
        print(excepted_message)
        context =  None
        status_flag = False
        message = "Password Reset Failed"
        status_code = status.HTTP_400_BAD_REQUEST
        context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
        return Response(status=status_code, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def change_password(request):
    data = request.data.copy()
    try:
        user = User.objects.get(id=request.user.id)

        email = request.user.email
        password = data['oldPassword']
        if email and password:
            user = authenticate(request=request, email=str(email).strip().lower(), password=password)
        
        if not user:
            context = None
            status_flag = False
            message = "Old Password is not a correct one"
            status_code = status.HTTP_400_BAD_REQUEST
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)
        
        if not data["newPasswordConfirmation"] == data["newPassword"]:
            context = None
            status_flag = False
            message = "New Password and New Confirmation Password are not Matching"
            status_code = status.HTTP_406_NOT_ACCEPTABLE
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)
    
        user.set_password(data["newPassword"])
        user.save()

        context = None
        status_flag = True
        message = 'Password Changed successfully'
        status_code = status.HTTP_200_OK
        context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
        return Response(status=status_code, data= context)

    except Exception as excepted_message:
        print(excepted_message)
        context =  None
        status_flag = False
        message = "Password Reset Failed"
        status_code = status.HTTP_400_BAD_REQUEST
        context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
        return Response(status=status_code, data= context)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def associates(request):
    try:
        user = request.user
        if request.method == 'GET':
            query_set = Associate.objects.all().order_by("-created_at")#.exclude(user__email=user.email)
            associates_data = AssociateSerializer(query_set, many=True).data

            context = associates_data
            status_flag = True
            message = None
            status_code = status.HTTP_200_OK
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)

        elif request.method == "POST":
            data = request.data.copy()
            if not request.user.is_superuser:
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)
            
            if "associateId" not in data.keys() or data["associateId"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"Associate Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            associate_ins = Associate.objects.get(id=data["associateId"])
            associate_ins.delete()

            query_set = Associate.objects.all().order_by("-created_at")#.exclude(user__email=request.user.email)
            associates_data = AssociateSerializer(query_set, many=True).data

            context = associates_data
            status_flag = True
            message = "Deleted successfully"
            status_code = status.HTTP_200_OK
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)
            
        else:
            context = None
            status_flag = False
            message = "Only Get and Post Method available"
            status_code = status.HTTP_405_METHOD_NOT_ALLOWED
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)

    except Exception as excepted_message:
        print(excepted_message)
        context = None
        status_flag = False
        message = str(excepted_message)
        status_code = status.HTTP_400_BAD_REQUEST
        context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
        return Response(status=status_code, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def users(request):
    try:
        request_data = request.data.copy()
        user = request.user
       
        if request.method == "POST":
            data = request.data.copy()
            if not request.user.is_admin:
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)

            request_data_filter = {}
            
            if request_data["name"] == "Appointment Date":
                if request_data["search"]:
                    search_date = datetime.strptime(request_data["search"], "%m/%d/%Y")

                    if request_data["criteria"] == "Contains":
                        request_data_filter =  {"tax_filings__isnull":False, "tax_filings__appointments__isnull":False, "tax_filings__appointments__status":"BOOKED", "tax_filings__appointments__start_time__date__contains":search_date.date()}
                    elif request_data["criteria"] == "Greater than and Equals to":
                        request_data_filter =  {"tax_filings__isnull":False, "tax_filings__appointments__isnull":False, "tax_filings__appointments__status":"BOOKED", "tax_filings__appointments__start_time__date__gte":search_date.date()}
                    elif request_data["criteria"] == "Equals to":
                        request_data_filter =  {"tax_filings__isnull":False, "tax_filings__appointments__isnull":False, "tax_filings__appointments__status":"BOOKED", "tax_filings__appointments__start_time__date":search_date.date()}
            else :
                if request_data["criteria"] == "Equals to":
                    if request_data["name"] == "First Name":
                        request_data_filter = {"first_name": request_data['search']}
                    elif request_data["name"] == "Last Name":
                        request_data_filter = {"last_name": request_data['search']}
                    elif request_data["name"] == "Email Id":
                        request_data_filter = {"email": request_data['search']}
                 
                elif request_data["criteria"] == "Contains":
                    if request_data["name"] == "First Name":
                        request_data_filter = {"first_name__contains": request_data['search']}
                    elif request_data["name"] == "Last Name":
                        request_data_filter = {"last_name__contains": request_data['search']}
                    elif request_data["name"] == "Email Id":
                        request_data_filter = {"email__contains": request_data['search']}

            if request_data["year"] != "All":
                request_data_filter.update({"tax_filings__isnull":False, "tax_filings__year__name":request_data["year"]})
                  
            query_set = User.objects.filter(**request_data_filter).order_by("-created_at")#.exclude(role="ADMIN")
            users_data = UserTaxFilingSerializer(query_set, many=True, context=request_data).data

            context = users_data
            status_flag = True
            message = None
            status_code = status.HTTP_200_OK
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)
            
        else:
            context = None
            status_flag = False
            message = "Only Get and Post Method available"
            status_code = status.HTTP_405_METHOD_NOT_ALLOWED
            context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
            return Response(status=status_code, data= context)

    except Exception as excepted_message:
        print(excepted_message)
        context = None
        status_flag = False
        message = str(excepted_message)
        status_code = status.HTTP_400_BAD_REQUEST
        context = {"data":context, "status_flag":status_flag, "status":status_code, "message":message}
        return Response(status=status_code, data= context)