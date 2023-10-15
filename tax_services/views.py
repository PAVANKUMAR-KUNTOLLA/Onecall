import os
import io
import re
import copy
import datetime
from django.db import transaction

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from users.models import *
from .models import *

from .helpers import  get_consolidated_data
from .serializers import TaxFilingSerializer, FinancialYearSerializer

# Create your views here.

def index(request):
    context = {"title":"Duiqo", "login_page_url":"http://127.0.0.1:8000/app/home/"}
    return render(request, 'index_prev.html', context)

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
            if "id" not in data.keys() and data["year"]:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"Name of the Tax Year Service is Required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)

            year = FinancialYear.objects.get(name=data["year"])
            user = User.objects.get(id=request.user.id)
            tax_filing = TaxFiling.objects.create(user=user, year=year)
            tax_filing.save()

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
            
            data = get_consolidated_data(data["id"])
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
            if 'id' not in data.keys():
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"Tax Filing Id is required"}
                return Response(status=status.HTTP_400_BAD_REQUEST, data= context)
            print(data)
            tax_filing_ins = TaxFiling.objects.get(id=data["id"])
            
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
                    user_ins.dob = datetime.datetime.strptime(data["dateOfBirth"], "%Y-%m-%d")
                if user_ins.gender !=  data["gender"]:
                    user_ins.gender =  data["gender"]
                if user_ins.job_title != data["occupation"]:
                    user_ins.job_title = data["occupation"]
                if user_ins.residental_status != data["residentialStatus"]:
                    user_ins.residental_status =  data["residentialStatus"]
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
                
                if user_ins.status == "MARRIED"and user_ins.spouse or any([data[each] != None for each in["spouseFirstName", "spouseMiddleInitial", "spouseLastName", "spouseSsnOrItin", "spouseDateOfBirth", "spouseGender", "spouseOccupation", "spouseEmail"]]):
                    if not user_ins.spouse:
                        # If the contact object doesn't exist, create a new one
                        spouse_ins = User.objects.create(
                            first_name = data["spouseFirstName"],
                            middle_name = data["spouseMiddleInitial"],
                            last_name = data["spouseLastName"],
                            ssn = data["spouseSsnOrItin"],
                            dob = datetime.datetime.strptime(data["spouseDateOfBirth"], "%Y-%m-%d"),
                            gender = data["spouseGender"],
                            job_title = data["spouseOccupation"],
                            residental_status = data["spouseResidentialStatus"],
                            email = data["spouseEmail"],
                            role="CLIENT",
                            status="MARRIED",
                            password="welcome")
                        
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
                        # if data["applyForItin"] == False: 
                        #     spouse_ins.applyForItin = False
                        if spouse_ins.dob != data["spouseDateOfBirth"]:
                            spouse_ins.dob = datetime.datetime.strptime(data["spouseDateOfBirth"], "%Y-%m-%d")
                        if spouse_ins.gender != data["spouseGender"]:
                            spouse_ins.gender = data["spouseGender"]
                        if spouse_ins.job_title != data["spouseOccupation"]:
                            spouse_ins.job_title = data["spouseOccupation"]
                        if spouse_ins.status != data["spouseResidentialStatus"]:
                            spouse_ins.status = data["spouseResidentialStatus"]
                        if spouse_ins.email != data["spouseEmail"]:
                            spouse_ins.email = data["spouseEmail"]

                        spouse_ins.save() 
                if tax_filing_ins.dependants and len(list(tax_filing_ins.dependants.all())) > 0 or any([data[each] != None for each in ["additionalFirstName", "additionaMiddleInitial", "additionalLasteName", "additionalSsnOrItin", "additionalDateOfBirth", "additionalResidentalStatus"]]):
                    dependants = tax_filing_ins.dependants.all()
                    for dependant_ins in dependants:
                        data["providedLivingSupport"]= True
                        data["additionalFirstName"]= dependant_ins.first_name
                        data["additionalMiddleInitial"]= dependant_ins.middle_name
                        data["additionalLastName"]= dependant_ins.last_name
                        data["additionalSsnOrItin"]= dependant_ins.ssn
                        data["applyForItin"]= False
                        data["additionalDateOfBirth"]= dependant_ins.dob
                        data["additionalGender"]= ""
                        data["additionalOccupation"]= ""
                        data["additionalResidentialStatus"]= ""
                        data["additionalEmail"]= ""

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

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def dependant_details(request):
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

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def bank_details(request):
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

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def income_details(request):
    data = request.data.copy()
    try:
        if request.method == "GET":
            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
            return Response(status=status.HTTP_200_OK, data= context)
        elif request.method == "POST":
            #//Income Details
            if tax_filing_ins.income:
                data["interestIncome"]= tax_filing_ins.income.interest_income
                data["dividendIncome"]= tax_filing_ins.income.dividend_income
                data["soldStocks"]= tax_filing_ins.income.sold_stocks
                data["soldCrypto"]= tax_filing_ins.income.sold_cryptocurrency
                data["foreignIncome"]= tax_filing_ins.income.foreign_country_income
                data["retirementAccounts"]= tax_filing_ins.income.other_benefits
                data["stateTaxRefund"]= tax_filing_ins.income.last_year_state_tax_refunds
                data["foreignBankAccount"]= tax_filing_ins.income.foreign_banks_account_balance_exceeding_10000
                data["foreignAssets"]= tax_filing_ins.income.foreign_assets_value_exceeding_50000
                data["rentalIncome"]= tax_filing_ins.income.rental_income_in_usa
                data["income1099"]= tax_filing_ins.income.last_year_1099_misc_nec_income
                data["incomeDescription"]=tax_filing_ins.income.income_description
                data["incomeAmount"]= tax_filing_ins.income.income_amount
                data["taxFiledLastYear"]= tax_filing_ins.income.filed_taxes_last_year
            else:
                data["interestIncome"]= False
                data["dividendIncome"]= False
                data["soldStocks"]= False
                data["soldCrypto"]= False
                data["foreignIncome"]= False
                data["retirementAccounts"]= False
                data["stateTaxRefund"]= False
                data["foreignBankAccount"]= False
                data["foreignAssets"]= False
                data["rentalIncome"]= False
                data["income1099"]= False
                data["incomeDescription"]= ""
                data["incomeAmount"]= ""
                data["taxFiledLastYear"]= False

            context = {"data":None, "status_flag":True, "status":status.HTTP_200_OK, "message":None}
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
            data["residentalChoices"] = [each[0] for each in residental_status_CHOICES]
            data["maritalChoices"] = [each[0] for each in MARITAL_CHOICES]
            data["visaTypeChoices"] = [each[0] for each in VISA_TYPE_CHOICES]
            data["refundChoices"] = [each[0] for each in REFUND_CHOICES]
            data["ownershipChoices"] = [each[0] for each in OWNERSHIP_CHOICES]
            data["refundChoices"] = [each[0] for each in REFUND_CHOICES]
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