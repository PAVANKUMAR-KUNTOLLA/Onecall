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
            if "id" not in data.keys() and not data["year"]:
                context = {"data":None, "status_flag":False, "status":status.HTTP_400_BAD_REQUEST, "message":"Name of the Tax Year Service is Required"}
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
                            spouse_ins = User.objects.create(
                                first_name = data["spouseFirstName"],
                                middle_name = data["spouseMiddleInitial"],
                                last_name = data["spouseLastName"],
                                ssn = data["spouseSsnOrItin"],
                                dob = datetime.datetime.strptime(data["spouseDateOfBirth"], "%Y-%m-%d"),
                                gender = data["spouseGender"],
                                job_title = data["spouseOccupation"],
                                residential_status = data["spouseResidentialStatus"],
                                email = data["spouseEmail"],
                                apply_for_itin=data["spouseApplyForItin"],
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
                        if spouse_ins.apply_for_itin != data["spouseApplyForItin"]:
                            spouse_ins.apply_for_itin = data["spouseApplyForItin"]

                        spouse_ins.save() 
            
                if len(tax_filing_ins.dependants.all()) > 0 or any([data[each] !=None and data[each] !=False for each in ["additionalFirstName", "additionalMiddleInitial", "additionalLastName", "additionalSsnOrItin", "additionalDateOfBirth", "additionalGender", "additionalOccupation", "additionalEmail", "additionalApplyForItin", "additionalStayCount", "additionalRelationship", "additionalVisaType"]]):
                    if len(tax_filing_ins.dependants.all()) == 0:
                        dependant_ins = Dependant.objects.create(
                                filing=tax_filing_ins,
                                first_name=data["additionalFirstName"],
                                middle_name=data["additionalMiddleInitial"],
                                last_name=data["additionalLastName"],
                                ssn=data["additionalSsnOrItin"],
                                dob=datetime.datetime.strptime(data["additionalDateOfBirth"], "%Y-%m-%d"),
                                gender=data["additionalGender"],
                                job_title=data["additionalOccupation"],
                                email=data["additionalEmail"],
                                apply_for_itin=data["additionalApplyForItin"],
                                relationship=data["additionalRelationship"],
                                stay_period=data["additionalStayCount"],
                                visa_type=data["additionalVisaType"]
                            )
                        dependant_ins.save()
                        tax_filing_ins.dependants.add(dependant_ins.id)
                        tax_filing_ins.save()

                    else:
                        dependants = tax_filing_ins.dependants.all()
                        for dependant_ins in dependants:
                            if dependant_ins.first_name != data["additionalFirstName"]:
                                dependant_ins.first_name = data["additionalFirstName"]
                            if dependant_ins.middle_name != data["additionalMiddleInitial"]:
                                dependant_ins.middle_name = data["additionalMiddleInitial"]
                            if dependant_ins.last_name != data["additionalLastName"]:
                                dependant_ins.last_name = data["additionalLastName"]
                            if dependant_ins.ssn != data["additionalSsnOrItin"]:
                                dependant_ins.ssn = data["additionalSsnOrItin"]
                            if dependant_ins.dob != data["additionalDateOfBirth"]:
                                dependant_ins.dob = datetime.datetime.strptime(data["additionalDateOfBirth"], "%Y-%m-%d")
                            if dependant_ins.gender != data["additionalGender"]:
                                dependant_ins.gender = data["additionalGender"]
                            if dependant_ins.job_title != data["additionalOccupation"]:
                                dependant_ins.job_title = data["additionalOccupation"]
                            if dependant_ins.email != data["additionalEmail"]:
                                dependant_ins.email = data["additionalEmail"]
                            if dependant_ins.apply_for_itin != data["additionalApplyForItin"]:
                                dependant_ins.apply_for_itin = data["additionalApplyForItin"]
                            if dependant_ins.relationship != data["additionalRelationship"]:
                                dependant_ins.relationship =data["additionalRelationship"]
                            if dependant_ins.stay_period != data["additionalStayCount"]:
                                dependant_ins.stay_period = data["additionalStayCount"]
                            if dependant_ins.visa_type != data["additionalVisaType"]:
                                dependant_ins.visa_type = data["additionalVisaType"]    
                            dependant_ins.save()
                
                if tax_filing_ins.income:
                    if data["taxFiledLastYear"] is not None and data["taxFiledLastYear"] != income_ins.filed_taxes_last_year:
                                income_ins.filed_taxes_last_year = data["taxFiledLastYear"]
                    else:
                        if data["taxFiledLastYear"]:
                            tax_filed_last_year = True if data["taxFiledLastYear"] == "true" or data["taxFiledLastYear"] == True else False
                            income_ins = Income.objects.create(
                                filing=tax_filing_ins,filed_taxes_last_year=tax_filed_last_year
                            )
                            income_ins.save()
                            tax_filing_ins.income = income_ins.id
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

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def bank_details(request):
    data = request.data.copy()
    try:
        if request.method == "POST":

            tax_filing_ins = TaxFiling.objects.get(id=data["id"])
            
            del data["id"]

            for key, value in data.items():
                if value == "true":
                    data[key] = True
                elif value=="false":
                    data["key"] = False
                elif value == "":
                    data[key]=None
            
            user_ins = User.objects.get(id=request.user.id)
            print(data)

            
                # Create a new BankModel instance if validations pass
            if not tax_filing_ins.bank and data["bankingType"] != "PAPER CHECK":
                if(  data["bankName"]
                    and data["accountHolderName"]
                    and data["ownership"]
                    and data["routingNumber"]
                    and data["accountNumber"]
                    and data["accountType"]
                    and data["routingNumber"] == data["confirmRoutingNumber"]
                    and data["accountNumber"] == data["confirmAccountNumber"]
                    and data["accountType"] == data["confirmAccountType"] 
                ):
                    bank_ins = Bank.objects.create(
                        filing=tax_filing_ins,
                        name=data["bankName"],
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
                if data["bankName"] != tax_filing_ins.bank.name:
                    tax_filing_ins.bank.name = data["bankName"]
                if data["accountHolderName"] != tax_filing_ins.bank.acc_holder_name:
                    tax_filing_ins.bank.acc_holder_name = data["accountHolderName"]
                if data["ownership"] != tax_filing_ins.bank.ownership:
                    tax_filing_ins.bank.ownership = data["ownership"]
                if data["routingNumber"] != tax_filing_ins.routing_number and data["routingNumber"] == data["confirmRoutingNumber"]:
                    tax_filing_ins.routing_number = data["routingNumber"]
                if data["accountNumber"] != tax_filing_ins.bank.account_number and data["accountNumber"] == data["confirmAccountNumber"]:
                    tax_filing_ins.bank.account_number = data["accountNumber"]
                if data["accountType"] != tax_filing_ins.bank.account_type:
                    tax_filing_ins.bank.account_type = data["accountType"]
                if data["confirmAccountType"] != tax_filing_ins.bank.account_type and data["accountType"] == data["confirmAccountType"]:
                    tax_filing_ins.bank.account_type = data["confirmAccountType"]

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
def income_details(request):
    data = request.data.copy()
    try:
        if request.method == "POST":
            #//Income Details
            tax_filing_ins = TaxFiling.objects.get(id=data["id"])
            
            del data["id"]

            for key, value in data.items():
                if value == "true":
                    data[key] = True
                elif value=="false":
                    data["key"] = False
                elif key == "incomeAmount" and value == "":
                    data[key]=0
            
            user_ins = User.objects.get(id=request.user.id)
            print(data)

            if not tax_filing_ins.income or any([data[each] is not None for each in ["interestIncome", "dividendIncome", "soldStocks", "soldCrypto", "foreignIncome", "retirementAccounts", "stateTaxRefund", "foreignBankAccount", "foreignAssets", "rentalIncome", "income1099", "incomeDescription", "incomeAmount"]]):
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
                        income_description=data["incomeDescription"],
                        income_amount=data["incomeAmount"],
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
                    if data["incomeDescription"] is not None and data["incomeDescription"] != income_ins.income_description:
                        income_ins.income_description = data["incomeDescription"]
                    if data["incomeAmount"] is not None and data["incomeAmount"] != income_ins.income_amount:
                        income_ins.income_amount = data["incomeAmount"]
                  
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