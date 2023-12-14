import os
import io
import re
import copy
import datetime
from os import listdir
from django.db import transaction
import pytz 
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from users.models import *
from .models import *

from django.core.mail import EmailMessage
from onecall.settings import MEDIA_ROOT, DEFAULT_FROM_EMAIL

from .helpers import  get_consolidated_data, income_details_data
from users.serializers import UserProfileSerializer
from .serializers import TaxFilingSerializer, FinancialYearSerializer,AppointmentSerializer,ReferalSerializer

# Create your views here.

def index(request):
    return render(request, 'index_prev.html')

def appointment(request):
    return render(request, 'appointment.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def refund_status(request):
    return render(request, 'refund-status.html')

def services(request):
    return render(request, 'services.html')

def tax_preparation_services(request):
    return render(request, 'tax-preparation-services.html')

def tax_planning_services(request):
    return render(request, 'tax-planning-services.html')

def business_consulting_services(request):
    return render(request, 'business-consulting-services.html')

def application(request):
    return render(request, 'index.html')

def serve_app(request, exception):
    return render(request, 'index.html')

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def my_services(request):
    data = request.data.copy()
    try:
        if request.method == "GET":
            queryset = TaxFiling.objects.filter(user__id=request.user.id)
            data = TaxFilingSerializer(queryset, many=True).data
            
            context = {"data":data, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        
        elif request.method == "POST":
            if "id" not in data.keys() and not data["year"]:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"Name of the Tax Year Service is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            if TaxFiling.objects.filter(user__id=request.user.id, year__name=data["year"]).exists():
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message": f'Tax Filing Service for year {data["year"]} is already Selected'}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)
            year = FinancialYear.objects.get(name=data["year"])
            user = User.objects.get(id=request.user.id)
            tax_filing_ins = TaxFiling.objects.create(user=user, year=year)
            tax_filing_ins.save()

            user.tax_filings.add(tax_filing_ins.id)
            user.save()

            queryset = TaxFiling.objects.filter(user__id=request.user.id)
            data = TaxFilingSerializer(queryset, many=True).data
            
            context = {"data":data, "status_flag":True, "status":status.HTTP_200_OK, "message":"created Successfully"}
            return Response(status=status.HTTP_200_OK, data= context)
        
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only GET & POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def tax_filing(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            if "id" not in data.keys():
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"Tax Filing Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data=context)

            tax_filing_ins = TaxFiling.objects.get(id=data["id"])

            if not (request.user.id ==  tax_filing_ins.user.id or request.user.is_admin):
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)
            
            data = get_consolidated_data(tax_filing_ins)
            context = {"data":data, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def personal_contact_details(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)
            tax_filing_ins = TaxFiling.objects.get(id=data["id"])

            if not (request.user.id ==  tax_filing_ins.user.id or request.user.is_admin):
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)
            
            del data["id"]

            for key, value in data.items():
                if value == "":
                    data[key] = None
            user_ins = User.objects.get(id=request.user.id)
            print(data)

            with transaction.atomic():
                #// Personal Details
                if user_ins.first_name !=  data["firstName"]:
                    user_ins.first_name = data["firstName"]
                if user_ins.middle_name != data["middleName"]:
                    user_ins.middle_name = data["middleName"]
                if user_ins.last_name !=  data["lastName"]:
                    user_ins.last_name =  data["lastName"]
                if user_ins.ssn !=  data["ssn"]:
                    user_ins.ssn =  data["ssn"]
                if user_ins.dob  != data["dateOfBirth"]:
                    user_ins.dob = datetime.datetime.strptime(data["dateOfBirth"], "%Y-%m-%dT%H:%M:%S.%fZ") + datetime.timedelta(seconds=19800)
                if user_ins.gender !=  data["gender"]:
                    user_ins.gender =  data["gender"]
                if user_ins.job_title != data["occupation"]:
                    user_ins.job_title = data["occupation"]
                if user_ins.residential_status != data["residentialStatus"]:
                    user_ins.residential_status =  data["residentialStatus"]
                if user_ins.status != data["taxPayerStatus"]:
                    user_ins.status =  data["taxPayerStatus"]
                
                user_ins.save()

                #// Contact Details
                if user_ins.contact or any([data[each] != None for each in ["street", "apartment","city","state","zipCode","country","primaryCountryCode","primaryPhoneNumber","secondaryCountryCode","secondaryPhoneNumber","contactEmail"]]):
                    if not user_ins.contact:
                        # If the contact object doesn't exist, create a new one
                        contact_ins = Contact.objects.create( user=user_ins,
                            street=data["street"],
                            apartment_no=data["apartment"],
                            city=data["city"],
                            state=data["state"],
                            zip_code=data["zipCode"],
                            country=data["country"],
                            primary_number_country_code=data["primaryCountryCode"],
                            primary_number=data["primaryPhoneNumber"],
                            secondary_number_country_code=data["secondaryCountryCode"],
                            secondary_number=data["secondaryPhoneNumber"])
                        
                        contact_ins.save()
                        user_ins.contact = contact_ins
                        user_ins.save()
                    else:
                        contact_ins = Contact.objects.get(user__id=request.user.id)
                        if contact_ins.street != data["street"]:
                            contact_ins.street = data["street"]
                        if contact_ins.apartment_no != data["apartment"]:
                            contact_ins.apartment_no = data["apartment"]
                        if contact_ins.city != data["city"]:
                            contact_ins.city = data["city"]
                        if contact_ins.state != data["state"]:
                            contact_ins.state = data["state"]
                        if contact_ins.zip_code != data["zipCode"]:
                            contact_ins.zip_code = data["zipCode"]
                        if contact_ins.country != data["country"]:
                            contact_ins.country = data["country"]
                        if contact_ins.primary_number_country_code != data["primaryCountryCode"]:
                            contact_ins.primary_number_country_code = data["primaryCountryCode"]
                        if contact_ins.primary_number != data["primaryPhoneNumber"]:
                            contact_ins.primary_number = data["primaryPhoneNumber"]
                        if contact_ins.secondary_number_country_code != data["secondaryCountryCode"]:
                            contact_ins.secondary_number_country_code = data["secondaryCountryCode"]
                        if contact_ins.secondary_number != data["secondaryPhoneNumber"]:
                            contact_ins.secondary_number = data["secondaryPhoneNumber"]

                        contact_ins.save()
                
                if user_ins.status == "MARRIED" and user_ins.spouse or any([data[each] != None and data[each] !=False for each in["spouseFirstName", "spouseMiddleInitial", "spouseLastName", "spouseSsnOrItin", "spouseDateOfBirth", "spouseGender", "spouseOccupation", "spouseEmail", "spouseApplyForItin"]]):
                    if not user_ins.spouse:
                        # If the contact object doesn't exist, create a new one
                        if User.objects.filter(email=data["spouseEmail"]).exists():
                            spouse_ins = User.objects.get(email=data["spouseEmail"])
                        else:
                            attribute_mapping = {
                                "first_name": "spouseFirstName",
                                "middle_name": "spouseMiddleInitial",
                                "last_name": "spouseLastName",
                                "ssn": "spouseSsnOrItin",
                                "dob": "spouseDateOfBirth",
                                "gender": "spouseGender",
                                "job_title": "spouseOccupation",
                                "email": "spouseEmail",
                                "apply_for_itin": "spouseApplyForItin",
                                "residential_status": "spouseVisaType",
                            }

                            # Remove the fields with None values from the request_data and map the attribute names
                            create_fields_spouse = {
                                model_attr: datetime.datetime.strptime(data[request_attr], "%Y-%m-%dT%H:%M:%S.%fZ") if request_attr == "spouseDateOfBirth" and data[request_attr] is not None else data[request_attr]
                                for model_attr, request_attr in attribute_mapping.items() 
                                if data[request_attr] is not None
                            }

                            # Creating the Dependant object with the non-None fields
                            spouse_ins = User.objects.create(**create_fields_spouse, role="CLIENT", status="MARRIED")
                            spouse_ins.set_password("welcome")
                            spouse_ins.save()
                        user_ins.spouse = spouse_ins
                        user_ins.save()
                    else:
                        spouse_ins = User.objects.get(id=request.user.spouse.id)
                        if spouse_ins.first_name != data["spouseFirstName"]:
                            spouse_ins.first_name = data["spouseFirstName"]
                        if spouse_ins.middle_name != data["spouseMiddleInitial"]:
                            spouse_ins.middle_name = data["spouseMiddleInitial"]
                        if spouse_ins.last_name != data["spouseLastName"]:
                            spouse_ins.last_name = data["spouseLastName"]
                        if spouse_ins.ssn != data["spouseSsnOrItin"]:
                            spouse_ins.ssn = data["spouseSsnOrItin"]
                        if spouse_ins.dob != data["spouseDateOfBirth"]:
                            spouse_ins.dob = datetime.datetime.strptime(data["spouseDateOfBirth"], "%Y-%m-%dT%H:%M:%S.%fZ") + datetime.timedelta(seconds=19800)
                        if spouse_ins.gender != data["spouseGender"]:
                            spouse_ins.gender = data["spouseGender"]
                        if spouse_ins.job_title != data["spouseOccupation"]:
                            spouse_ins.job_title = data["spouseOccupation"]
                        if spouse_ins.residential_status != data["spouseResidentialStatus"]:
                            spouse_ins.residential_status = data["spouseResidentialStatus"]
                        if spouse_ins.apply_for_itin != data["spouseApplyForItin"]:
                            spouse_ins.apply_for_itin = data["spouseApplyForItin"]

                        spouse_ins.save()
        
                if tax_filing_ins.income:
                    if data["taxFiledLastYear"] is not None and data["taxFiledLastYear"] != tax_filing_ins.income.filed_taxes_last_year:
                            tax_filing_ins.income.filed_taxes_last_year = data["taxFiledLastYear"]
                            tax_filing_ins.income.save()
                    else:
                        if data["taxFiledLastYear"]:
                            tax_filed_last_year = True if data["taxFiledLastYear"] == "true" or data["taxFiledLastYear"] == True else False
                            income_ins = Income.objects.create(
                                filing=tax_filing_ins,filed_taxes_last_year=tax_filed_last_year
                            )
                            income_ins.save()
                            tax_filing_ins.income = income_ins
                            tax_filing_ins.save()

            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def spouse_details(request):
    data = request.data.copy()
    try:
        if request.method == "GET":
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        elif request.method == "POST":
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only GET & POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_dependant(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)
            tax_filing_ins = TaxFiling.objects.get(id=data["id"])

            if not (request.user.id ==  tax_filing_ins.user.id or request.user.is_admin):
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)

            for key, value in data.items():
                if value == "":
                    data[key] = None
        
            if data["additionalSsnOrItin"] and Dependant.objects.filter(filing__id=tax_filing_ins.id, ssn=data["additionalSsnOrItin"]).exists():
                dependant_ins = Dependant.objects.get(filing__id=tax_filing_ins.id, ssn=data["additionalSsnOrItin"])
                update_fields = {}

                if data["additionalFirstName"] is not None and dependant_ins.first_name != data["additionalFirstName"]:
                    update_fields['first_name'] = data["additionalFirstName"]
                if data["additionalMiddleInitial"] is not None and dependant_ins.middle_name != data["additionalMiddleInitial"]:
                    update_fields['middle_name'] = data["additionalMiddleInitial"]
                if data["additionalLastName"] is not None and dependant_ins.last_name != data["additionalLastName"]:
                    update_fields['last_name'] = data["additionalLastName"]
                if data["additionalSsnOrItin"] is not None and dependant_ins.ssn != data["additionalSsnOrItin"]:
                    update_fields['ssn'] = data["additionalSsnOrItin"]
                if data["additionalDateOfBirth"] is not None and dependant_ins.dob != datetime.datetime.strptime(data["additionalDateOfBirth"], "%Y-%m-%dT%H:%M:%S.%fZ"):
                    update_fields['dob'] = datetime.datetime.strptime(data["additionalDateOfBirth"], "%Y-%m-%dT%H:%M:%S.%fZ") + datetime.timedelta(seconds=19800)
                if data["additionalGender"] is not None and dependant_ins.gender != data["additionalGender"]:
                    update_fields['gender'] = data["additionalGender"]
                if data["additionalOccupation"] is not None and dependant_ins.job_title != data["additionalOccupation"]:
                    update_fields['job_title'] = data["additionalOccupation"]
                if data["additionalEmail"] is not None and dependant_ins.email != data["additionalEmail"]:
                    update_fields['email'] = data["additionalEmail"]
                if data["additionalApplyForItin"] is not None and dependant_ins.apply_for_itin != data["additionalApplyForItin"]:
                    update_fields['apply_for_itin'] = data["additionalApplyForItin"]
                if data["additionalRelationship"] is not None and dependant_ins.relationship != data["additionalRelationship"]:
                    update_fields['relationship'] = data["additionalRelationship"]
                if data["additionalStayCount"] is not None and dependant_ins.stay_period != data["additionalStayCount"]:
                    update_fields['stay_period'] = data["additionalStayCount"]
                if data["additionalVisaType"] is not None and dependant_ins.visa_type != data["additionalVisaType"]:
                    update_fields['visa_type'] = data["additionalVisaType"]

                if update_fields:
                    dependant_ins.__dict__.update(update_fields)
                    dependant_ins.save()
            else:
                attribute_mapping = {
                    "first_name": "additionalFirstName",
                    "middle_name": "additionalMiddleInitial",
                    "last_name": "additionalLastName",
                    "ssn": "additionalSsnOrItin",
                    "dob": "additionalDateOfBirth",
                    "gender": "additionalGender",
                    "job_title": "additionalOccupation",
                    "email": "additionalEmail",
                    "apply_for_itin": "additionalApplyForItin",
                    "relationship": "additionalRelationship",
                    "stay_period": "additionalStayCount",
                    "visa_type": "additionalVisaType",
                }

                # Remove the fields with None values from the request_data and map the attribute names
                create_fields_dependant = {
                    model_attr: datetime.datetime.strptime(data[request_attr], "%Y-%m-%dT%H:%M:%S.%fZ") if request_attr == "additionalDateOfBirth" and data[request_attr] is not None else data[request_attr]
                    for model_attr, request_attr in attribute_mapping.items() 
                    if data[request_attr] is not None
                }

                # Creating the Dependant object with the non-None fields
                dependant_ins = Dependant.objects.create(filing=tax_filing_ins, **create_fields_dependant)
                dependant_ins.save()
                tax_filing_ins.dependants.add(dependant_ins.id)
                tax_filing_ins.save()

            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":"Success"}
            return Response(status=status.HTTP_200_OK, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def dependant_details(request):
    data = request.data.copy()
    try:
        if request.method == "POST":

            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            tax_filing_ins = TaxFiling.objects.get(id=data["id"])

            if not (request.user.id ==  tax_filing_ins.user.id or request.user.is_admin):
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)
            return_dict = list()
            dependants = tax_filing_ins.dependants.all()
            
            for dependant_ins in dependants:
                each_dict = dict()
                each_dict["id"] = dependant_ins.id
                each_dict["additionalFirstName"]= dependant_ins.first_name
                each_dict["additionalMiddleInitial"]= dependant_ins.middle_name
                each_dict["additionalLastName"]= dependant_ins.last_name
                each_dict["additionalSsnOrItin"]= dependant_ins.ssn
                each_dict["additionalApplyForItin"]= dependant_ins.apply_for_itin
                each_dict["additionalDateOfBirth"]= dependant_ins.dob
                each_dict["additionalGender"]= dependant_ins.gender
                each_dict["additionalOccupation"]= dependant_ins.job_title
                each_dict["additionalVisaType"]= dependant_ins.visa_type
                each_dict["additionalEmail"]= dependant_ins.email
                each_dict["additionalRelationship"]= dependant_ins.relationship
                each_dict["additionalStayCount"]= dependant_ins.stay_period
                return_dict.append(each_dict)

            context = {"data":return_dict, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_dependant(request):
    data = request.data.copy()
    try:
        if request.method == "POST":

            if "taxFilingId" not in data.keys() or data["taxFilingId"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"Dependant Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            tax_filing_ins = TaxFiling.objects.get(id=data["taxFilingId"])
            dependant_ins = Dependant.objects.get(id=data["id"])
            tax_filing_ins.dependants.remove(dependant_ins.id)
            tax_filing_ins.save()
            
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":"Deleted Successfully"}
            return Response(status=status.HTTP_200_OK, data= context)

            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def bank_details(request):
    data = request.data.copy()
    try:
        if request.method == "POST":

            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            tax_filing_ins = TaxFiling.objects.get(id=data["id"])

            if not (request.user.id ==  tax_filing_ins.user.id or request.user.is_admin):
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)
            
            del data["id"]

            for key, value in data.items():
                if value == "true":
                    data[key] = True
                elif value=="false":
                    data[key] = False
                elif value == "":
                    data[key]=None
            
            user_ins = User.objects.get(id=request.user.id)
            print(data)

            # Create a new BankModel instance if validations pass
            if not tax_filing_ins.bank and data["bankingType"] != "PAPER CHECK":
                if(data["bankName"] and data["accountHolderName"]
                    and data["ownership"] and data["routingNumber"]
                    and data["accountNumber"] and data["accountType"]
                    and data["routingNumber"] == data["confirmRoutingNumber"]
                    and data["accountNumber"] == data["confirmAccountNumber"]
                    and data["accountType"] == data["confirmAccountType"]
                ):
                    bank_ins = Bank.objects.create(
                        filing=tax_filing_ins,
                        bank_name=data["bankName"],
                        acc_holder_name=data["accountHolderName"],
                        ownership=data["ownership"],
                        routing_number=data["routingNumber"],
                        account_number=data["accountNumber"],
                        account_type=data["accountType"]
                    )
                    bank_ins.save()
                    tax_filing_ins.bank = bank_ins
                    tax_filing_ins.save()
  
            elif tax_filing_ins.bank:
                if data["bankName"] != tax_filing_ins.bank.bank_name:
                    tax_filing_ins.bank.bank_name = data["bankName"]
                if data["accountHolderName"] != tax_filing_ins.bank.acc_holder_name:
                    tax_filing_ins.bank.acc_holder_name = data["accountHolderName"]
                if data["ownership"] != tax_filing_ins.bank.ownership:
                    tax_filing_ins.bank.ownership = data["ownership"]
                if data["routingNumber"] != tax_filing_ins.bank.routing_number and data["routingNumber"] == data["confirmRoutingNumber"]:
                    tax_filing_ins.bank.routing_number = data["routingNumber"]
                if data["accountNumber"] != tax_filing_ins.bank.account_number and data["accountNumber"] == data["confirmAccountNumber"]:
                    tax_filing_ins.bank.account_number = data["accountNumber"]
                if data["accountType"] != tax_filing_ins.bank.account_type:
                    tax_filing_ins.bank.account_type = data["accountType"]
                if data["confirmAccountType"] != tax_filing_ins.bank.account_type and data["accountType"] == data["confirmAccountType"]:
                    tax_filing_ins.bank.account_type = data["confirmAccountType"]
                tax_filing_ins.bank.save()
            if tax_filing_ins.refund_type != data["bankingType"] and data["bankingType"]:
                tax_filing_ins.refund_type = data["bankingType"]
                tax_filing_ins.save()

            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def other_income_details(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            #//Income Details

            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            tax_filing_ins = TaxFiling.objects.get(id=data["id"])

            if not (request.user.id ==  tax_filing_ins.user.id or request.user.is_admin):
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)
            
            if "type" in data.keys() and data["type"] == "delete":
                if "otherIncomeId" not in data.keys() or data["id"] == None:
                    context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"Other Income Id is Required"}
                    return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

                other_income_ins = OtherIncome.objects.get(id=data["otherIncomeId"])
                tax_filing_ins.other_incomes.remove(other_income_ins.id)
                tax_filing_ins.save()
                other_income_ins.delete()

            return_dict = income_details_data(tax_filing_ins)
        
            context = {"data":return_dict, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only GET & POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def income_details(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            #//Income Details

            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            tax_filing_ins = TaxFiling.objects.get(id=data["id"])

            if not (request.user.id ==  tax_filing_ins.user.id or request.user.is_admin):
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)
            
            del data["id"]

            for key, value in data.items():
                if value == "true":
                    data[key] = True
                elif value=="false":
                    data[key] = False
                elif key == "incomeAmount" and value == "":
                    data[key]=0
            
            user_ins = User.objects.get(id=request.user.id)
            print(data)

            if "type" in data.keys() and data["type"] == "otherIncome":
              
                income_ins = OtherIncome.objects.create(
                    filing=tax_filing_ins,
                    income_description=data["incomeDescription"],
                    income_amount=data["incomeAmount"]
                )
                income_ins.save()
                tax_filing_ins.other_incomes.add(income_ins.id)
                tax_filing_ins.save()

            else:
                if not tax_filing_ins.income or any([data[each] is not None for each in ["interestIncome", "dividendIncome", "soldStocks", "soldCrypto", "foreignIncome", "retirementAccounts", "stateTaxRefund", "foreignBankAccount", "foreignAssets", "rentalIncome", "income1099"]]):
                    if not tax_filing_ins.income:
                        income_ins = Income.objects.create(
                            filing=tax_filing_ins,
                            interest_income=data["interestIncome"],
                            dividend_income=data["dividendIncome"],
                            sold_stocks=data["soldStocks"],
                            sold_cryptocurrency=data["soldCrypto"],
                            foreign_country_income=data["foreignIncome"],
                            other_benefits=data["retirementAccounts"],
                            last_year_state_tax_refunds=data["stateTaxRefund"],
                            foreign_banks_account_balance_exceeding_10000=data["foreignBankAccount"],
                            foreign_assets_value_exceeding_50000=data["foreignAssets"],
                            rental_income_in_usa=data["rentalIncome"],
                            last_year_1099_misc_nec_income=data["income1099"],
                        )
                        income_ins.save()
                        tax_filing_ins.income = income_ins
                        tax_filing_ins.save()

                    else:
                        income_ins = Income.objects.get(id=tax_filing_ins.income.id)
                        if data["interestIncome"] is not None and data["interestIncome"] != income_ins.interest_income:
                            income_ins.interest_income = data["interestIncome"]
                        if data["dividendIncome"] is not None and data["dividendIncome"] != income_ins.dividend_income:
                            income_ins.dividend_income = data["dividendIncome"]
                        if data["soldStocks"] is not None and data["soldStocks"] != income_ins.sold_stocks:
                            income_ins.sold_stocks = data["soldStocks"]
                        if data["soldCrypto"] is not None and data["soldCrypto"] != income_ins.sold_cryptocurrency:
                            income_ins.sold_cryptocurrency = data["soldCrypto"]
                        if data["foreignIncome"] is not None and data["foreignIncome"] != income_ins.foreign_country_income:
                            income_ins.foreign_country_income = data["foreignIncome"]
                        if data["retirementAccounts"] is not None and data["retirementAccounts"] != income_ins.other_benefits:
                            income_ins.other_benefits = data["retirementAccounts"]
                        if data["stateTaxRefund"] is not None and data["stateTaxRefund"] != income_ins.last_year_state_tax_refunds:
                            income_ins.last_year_state_tax_refunds = data["stateTaxRefund"]
                        if data["foreignBankAccount"] is not None and data["foreignBankAccount"] != income_ins.foreign_banks_account_balance_exceeding_10000:
                            income_ins.foreign_banks_account_balance_exceeding_10000 = data["foreignBankAccount"]
                        if data["foreignAssets"] is not None and data["foreignAssets"] != income_ins.foreign_assets_value_exceeding_50000:
                            income_ins.foreign_assets_value_exceeding_50000 = data["foreignAssets"]
                        if data["rentalIncome"] is not None and data["rentalIncome"] != income_ins.rental_income_in_usa:
                            income_ins.rental_income_in_usa = data["rentalIncome"]
                        if data["income1099"] is not None and data["income1099"] != income_ins.last_year_1099_misc_nec_income:
                            income_ins.last_year_1099_misc_nec_income = data["income1099"]
                    
                        income_ins.save()
                    
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only GET & POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def upload_tax_docs(request):
    data = request.data.copy()
    try:
        if request.method == "POST":

            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            tax_filing_ins = TaxFiling.objects.get(id=data["id"])

            if not (request.user.id ==  tax_filing_ins.user.id or request.user.is_admin):
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)

            if request.FILES:
                # Access the uploaded file from request.FILES
                uploaded_file = request.FILES['upload']
                if data["type"] == "docs":
                    tax_docs_ins = TaxDocs.objects.create(filing=tax_filing_ins, file_name=uploaded_file)
                    tax_docs_ins.save()
                    tax_filing_ins.tax_docs.add(tax_docs_ins.id)
                    tax_filing_ins.save()
                elif data["type"] == "returns":
                    tax_returns_ins = TaxReturns.objects.create(filing=tax_filing_ins, file_name=uploaded_file, remarks=data["remarks"])
                    tax_returns_ins.save()

                    tax_filing_ins.tax_returns.add(tax_returns_ins.id)
                    tax_filing_ins.save()
                else:
                    context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"Type of Docs is Required"}
                    return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

                context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":"Upload Done Successfully"}
                return Response(status=status.HTTP_200_OK, data= context)
            else:
                return_dict = list()

                # Return the file associated with tax_filing_ins.tax_docs
                if data["type"] == "docs" and tax_filing_ins.tax_docs:
                    tax_docs = tax_filing_ins.tax_docs.all()

                    if tax_docs:
                        for each in tax_docs:
                            # Prepare the response data for the associated file
                            file_name = each.file_name.name  # Get the file name
                            file_size_in_bytes = os.path.getsize(each.file_name.path)
                            file_size_kb = round(file_size_in_bytes / 1024, 2)
                            file_size_mb = round(file_size_in_bytes / (1024 * 1024), 2)
                            file_created_at = os.path.getctime(each.file_name.path)
                            upload_time = datetime.datetime.fromtimestamp(file_created_at).strftime("%Y-%m-%d %H:%M:%S")

                            each_file_dict = {
                                "id":each.id,
                                "file_name": file_name.replace("TaxDocs/", ""),
                                "upload_time": upload_time,
                                "file_size": f'{file_size_kb} (KB)/{file_size_mb} (MB)'
                            }

                            return_dict.append( each_file_dict)

                elif data["type"] == "returns" and tax_filing_ins.tax_returns:
                    tax_returns = tax_filing_ins.tax_returns.all()

                    if tax_returns:
                        for each in tax_returns:
                            # Prepare the response data for the associated file
                            file_name = each.file_name.name  # Get the file name
                            file_size_in_bytes = os.path.getsize(each.file_name.path)
                            file_size_kb = round(file_size_in_bytes / 1024, 2)
                            file_size_mb = round(file_size_in_bytes / (1024 * 1024), 2)
                            file_created_at = os.path.getctime(each.file_name.path)
                            upload_time = datetime.datetime.fromtimestamp(file_created_at).strftime("%Y-%m-%d %H:%M:%S")

                            each_file_dict = {
                                "id":each.id,
                                "file_name": file_name.replace("TaxReturns/", ""),
                                "upload_time": upload_time,
                                "remarks":each.remarks,
                                "file_size": f'{file_size_kb} (KB)/{file_size_mb} (MB)'
                            }

                            return_dict.append( each_file_dict)
                    
                context = {"data":return_dict, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
                return Response(status=status.HTTP_200_OK, data= context)
        
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only GET & POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def confirm_details(request):
    data = request.data.copy()
    try:
        if request.method == "GET":
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        elif request.method == "POST":
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only GET & POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['GET'])
def choice_data(request):
    data = request.data.copy()
    try:
        if request.method == "GET":
            data = dict()
            data["roleChoices"] = [each[0] for each in ROLE_CHOICES]
            data["genderChoices"] = [each[0] for each in GENDER_CHOICES]
            data["residentialChoices"] = [each[0] for each in residential_status_CHOICES]
            data["maritalChoices"] = [each[0] for each in MARITAL_CHOICES]
            data["visaTypeChoices"] = [each[0] for each in VISA_TYPE_CHOICES]
            data["refundChoices"] = [each[0] for each in refund_type]
            data["ownershipChoices"] = [each[0] for each in OWNERSHIP_CHOICES]
            data["refundChoices"] = [each[0] for each in refund_type]
            data["bankAccountTypeChoices"] = [each[0] for each in BANK_ACCOUNT_TYPE]
            data["appointmentStatusChoices"] = [each[0] for each in APPOINTMENT_STATUS_CHOICES]
            data["paymentStatusChoices"] = [each[0] for each in PAYMENT_STATUS_CHOICES]
            data["filingStatusChoices"] = [each[0] for each in FILING_STATUS_CHOICES]

            context = {"data":data, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only GET Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)
    
@api_view(['GET'])
def tax_years(request):
    data = request.data.copy()
    try:
        if request.method == "GET":
            data = FinancialYear.objects.all()
            data = FinancialYearSerializer(data, many=True).data
            context = {"data":data, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only GET Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def download_tax_docs(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            file_name = data["file_name"]
            file_parent_path = "TaxDocs" if data["type"] == "docs" else "TaxReturns"
            if os.path.exists((os.path.join(MEDIA_ROOT, file_parent_path, file_name))):
                # Reading the file that user has requested
                with open(os.path.join(MEDIA_ROOT, file_parent_path, file_name), 'rb') as f:
                    file_data = f.read()

                # Determine the file's content type based on the file extension
                file_extension = os.path.splitext(file_name)[1].lower()

                # Map file extensions to content types
                content_types = {
                    '.csv': 'text/csv',
                    '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                    '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    '.zip': 'application/zip',
                    # Add more file types and content types as needed
                }

                # Default to application/octet-stream if the file extension is not recognized
                content_type = content_types.get(file_extension, 'application/octet-stream')

                response = HttpResponse(file_data, content_type=content_type)
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'

                return response
            
            else:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"No files Found with the requested name"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_tax_docs(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            
            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            file_name = data["file_name"]
            file_parent_path = "TaxDocs" if data["type"] == "docs" else "TaxReturns"
           
            if os.path.exists((os.path.join(MEDIA_ROOT, file_parent_path, file_name))):
                
                tax_filing_ins = TaxFiling.objects.get(id=data["id"])

                if not (request.user.id ==  tax_filing_ins.user.id or request.user.is_admin):
                    context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                    return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)

                if data["type"] == "docs":
                    tax_docs_ins = TaxDocs.objects.get(id=data["file_id"])
                    tax_filing_ins.tax_docs.remove(tax_docs_ins.id)
                    tax_docs_ins.delete()

                elif data["type"] == "returns":
                    tax_returns_ins = TaxReturns.objects.get(id=data["file_id"])
                    tax_filing_ins.tax_returns.remove(tax_returns_ins.id)
                    tax_returns_ins.delete()

                tax_filing_ins.save()
                
                context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":"Deleted Successfully"}
                return Response(status=status.HTTP_200_OK, data= context)
            
            else:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"No files Found with the requested name"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def appointment_details(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            
            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            tax_filing_ins = TaxFiling.objects.get(id=data["id"])

            if not (request.user.id ==  tax_filing_ins.user.id or request.user.is_admin):
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)
            queryset = tax_filing_ins.appointments.all().order_by("-created_at")
            data = AppointmentSerializer(queryset, many=True).data
                
            context = {"data":data, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
            
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def latest_appointment(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            queryset = Appointment.objects.filter(filing__user__id=request.user.id,status="BOOKED").order_by("-created_at")
            data = AppointmentSerializer(queryset, many=True).data
                
            context = {"data":data, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
            
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_appointment(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            print(data)
            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            tax_filing_ins = TaxFiling.objects.get(id=data["id"])

            if tax_filing_ins.appointments and tax_filing_ins.appointments.filter(status="BOOKED").exists():
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"Please Cancel the existing appointment"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            if not (request.user.id ==  tax_filing_ins.user.id or request.user.is_admin):
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)
           
            # Parse the start time and date
            hours = int(data["time"].split(":")[0])*3600
            minutes = data["time"].split(":")[1]
            minutes = 0 if minutes == "00" else 1800
            start_datetime = datetime.datetime.strptime(data["date"], "%Y-%m-%dT%H:%M:%S.%fZ") + datetime.timedelta(seconds=19800) + datetime.timedelta(seconds=hours+minutes)

            # Calculate the end time by adding 30 minutes
            end_datetime = start_datetime + datetime.timedelta(minutes=30)

            # Create aware datetimes with the specified time zone
            # start_datetime_aware = pytz.timezone(data["timezone"]).localize(start_datetime)
            # end_datetime_aware = pytz.timezone(data["timezone"]).localize(end_datetime)

            # Create and save the appointment
            appointment_ins = Appointment.objects.create(filing=tax_filing_ins, start_time=start_datetime, end_time=end_datetime, time_zone=data["timezone"])
            appointment_ins.save()

            # Update the tax_filing_ins with the appointment
            tax_filing_ins.appointments.add(appointment_ins.id)
            tax_filing_ins.save()
            
            email=tax_filing_ins.user.email

            email_body = f'''Dear Client,

I hope this message finds you well. We are delighted that you've chosen our online appointment scheduling system, and I'm pleased to confirm that your appointment has been successfully booked and finalized.

Appointment Details:
Date: {datetime.datetime.strftime(appointment_ins.start_time,"%m-%d-%Y")}
Time: {datetime.datetime.strftime(appointment_ins.start_time,"%H:%M")}

During the tax interview, which is expected to last approximately 30 minutes, one of our tax associates will gather all the necessary information from you. We will meticulously review the details you provided on our website to ensure accurate reporting of all income details to the IRS. Additionally, we will diligently collect all eligible expenses that could potentially save you money on taxes. Following the call, if there are no pending information requirements from your end, our tax professionals will promptly work on estimating your refund and provide you with a quote within 3 to 4 hours.

Please make a note of the following information:
Feel free to review the specifics on our website or reach out to our support team if any particular requirements or preparations are necessary for your upcoming appointment. Our aim is to ensure a smooth and productive interview. Kindly inform us at your earliest convenience if there are any changes to your schedule or if a reschedule is needed.

Thank you for choosing One Call Tax Services for your Tax Preparation needs. We are eagerly looking forward to assisting you and ensuring a seamless experience. For any inquiries or concerns, please do not hesitate to contact our customer support at Support@octs.com or +1 664 248 1357.

Best regards,
ONE CALL TAX SERVICES INC
            '''

            subject = "Confirmation of Your Scheduled Appointment via Our Website"            
            from_email = DEFAULT_FROM_EMAIL
            to = [tax_filing_ins.user.email, ]
            email = EmailMessage(subject, email_body, from_email, to)
            email.send()
            
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":"Appointment Booked successfully"}
            return Response(status=status.HTTP_200_OK, data= context)
            
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_appointment(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            print(data)
            if "appointmentId" not in data.keys() or data["appointmentId"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"Appointment Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)
            
            if not request.user.is_admin:
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)

            appointment_ins = Appointment.objects.get(id=data["appointmentId"])

            start_date = data["date"]
            start_time = data["time"]

            # Parse the start time and date
            start_datetime = datetime.datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M")

            # Calculate the end time by adding 30 minutes
            end_datetime = start_datetime + datetime.timedelta(minutes=30)

            # Create aware datetimes with the specified time zone
            start_datetime_aware = pytz.timezone(appointment_ins.time_zone).localize(start_datetime)
            end_datetime_aware = pytz.timezone(appointment_ins.time_zone).localize(end_datetime)

            appointment_ins.start_time=start_datetime_aware
            appointment_ins.end_time=end_datetime_aware
            appointment_ins.save()
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":"Appointment Updated successfully"}
 
            return Response(status=status.HTTP_200_OK, data= context)
            
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_appointment(request):
    data = request.data.copy()
    try:
        if request.method == "POST":

            if "appointmentId" not in data.keys() or data["appointmentId"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"Appointment Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)
           
            appointment_ins = Appointment.objects.get(id=data["appointmentId"])
            appointment_ins.status="CANCELLED"
            appointment_ins.save()
            
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":"Deleted Successfully"}
            return Response(status=status.HTTP_200_OK, data= context)
            
           
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_refund(request):
    request_data = request.data.copy()
    try:
        if request.method == "POST":

            if not request.user.is_admin:
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)

            for index, data in enumerate(request_data):
                if "year" not in data.keys() or data["year"] == None:
                    context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Year is Required"}
                    return Response(status=status.HTTP_400_BAD_REQUEST, data= context)
                
                if not TaxFiling.objects.filter(user__id=data["id"], year__name=data["year"]).exists():
                    context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":f'TaxFiling for year {data["year"]} of this User is not Found'}
                    return Response(status=status.HTTP_400_BAD_REQUEST, data= context)
                
                tax_filing_ins = TaxFiling.objects.get(user__id=data["id"], year__name=data["year"])
                refund_ins = Refund.objects.create(filing=tax_filing_ins, service_type=data["service_type"], refund_type=data["refund_type"], standard_refund=data["standard_refund"], standard_fee=data["standard_fee"], itemized_refund=data["itemized_refund"], itemized_fee=data["itemized_fee"], discount=data["discount"], paid_advance=data["paid_advance"], max_itemized_refund=data["max_itemized_refund"], max_itemized_fee=data["max_itemized_fee"])
                refund_ins.save()
                tax_filing_ins.refunds.add(refund_ins.id)
                tax_filing_ins.save()
            
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":"Created Successfully"}
            return Response(status=status.HTTP_200_OK, data= context)
            
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def refunds(request):
    data = request.data.copy()
    try:
        if request.method == "POST":

            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"User Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            if not (request.user.id ==  data["id"] or request.user.is_admin):
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)

            data = Refund.objects.filter(filing__user__id=data["id"]).values()

            context = {"data":data, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
           
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_message(request):
    data = request.data.copy()
    try:
        if request.method == "POST":

            if not request.user.is_admin:
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)

            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            tax_filing_ins = TaxFiling.objects.get(id=data["id"])
            message_ins = Message.objects.create(filing=tax_filing_ins, message=data["message"])
            if User.objects.filter(email=data["by"]).exists():
                message_ins.by = User.obejcts.get(email=data["email"])
            message_ins.save()
            
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":"Created Successfully"}
            return Response(status=status.HTTP_200_OK, data= context)
            
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def messages(request):
    data = request.data.copy()
    try:
        if request.method == "POST":

            if "id" not in data.keys() or data["id"] == None:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"TaxFiling Id is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            tax_filing_ins = TaxFiling.objects.get(id=data["id"])

            if not (request.user.id ==  tax_filing_ins.user.id or request.user.is_admin):
                context = {"data":None, "status_flag":False, "status":status.HTTP_401_UNAUTHORIZED, "message":"UnAuthorized"}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=context)

            data = Message.objects.filter(filing__id=tax_filing_ins.id)

            context = {"data":data, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
           
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def referal_details(request):
    data = request.data.copy()
    try:
        if request.method == "GET":
            return_dict={"joined":list(),"not_joined":list()}
            referals = User.objects.filter(referred_by__id=request.user.id).order_by("-created_at")
            return_dict["joined"] = UserProfileSerializer(referals, many=True).data

            referals = Referal.objects.filter(referred_by=request.user.id).order_by("-created_at")
            for each in referals:
                if not User.objects.filter(email=each.email, referred_by__email=request.user.email):
                    referal_data = ReferalSerializer(each).data
                    return_dict["not_joined"].append(referal_data)
                
            context = {"data":return_dict, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
            
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only GET Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def make_referal(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            print(data)
           
            user_ins = User.objects.get(id=request.user.id)
            referal_ins = Referal.objects.create(referred_by=user_ins, first_name=data["firstName"],  last_name=data["lastName"],  email=data["email"], contact_no=data["contact"])
            referal_ins.save()

            email=data["email"]
            referral_id = request.user.referral_id

            referral_url = request.build_absolute_uri(f'/register/?email={email}&referralId={referral_id}')  

            email_body = f'Hello {email}, \n Use link below to register  \n\n' + f'You are referred to Onecall Tax Services INC by {request.user.email} \n\n Please register with below link (by clicking on the link) to file your taxes at Taxcooler Inc. \n\n' + \
                    referral_url + "\n\n Regards \nOnecall Tax Services Team"

            subject = "Register & File your taxes at Onecall Tax Services"            
            from_email = DEFAULT_FROM_EMAIL
            to = [data["email"], ]
            email = EmailMessage(subject, email_body, from_email, to)
            email.send()

            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":"Referal successfull"}
            return Response(status=status.HTTP_200_OK, data= context)
            
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def download_template(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            file_name = data["file_name"]
            if os.path.exists((os.path.join(MEDIA_ROOT, "templates", file_name))):
                # Reading the file that user has requested
                with open(os.path.join(MEDIA_ROOT, "templates", file_name), 'rb') as f:
                    file_data = f.read()

                # Determine the file's content type based on the file extension
                file_extension = os.path.splitext(file_name)[1].lower()

                # Map file extensions to content types
                content_types = {
                    '.csv': 'text/csv',
                    '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                    '.xls': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                    '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    '.zip': 'application/zip',
                    # Add more file types and content types as needed
                }

                # Default to application/octet-stream if the file extension is not recognized
                content_type = content_types.get(file_extension, 'application/octet-stream')

                response = HttpResponse(file_data, content_type=content_type)
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'

                return response
            
            else:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"No files Found with the requested name"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)
        else:
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message": "Only POST Method Available"}
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data= context)
    except Exception as excepted_message:
        print(str(excepted_message))
        context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":str(excepted_message)}
        return Response(status=status.HTTP_400_BAD_REQUEST, data= context)