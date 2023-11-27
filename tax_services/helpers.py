from .models import *
from datetime import datetime
def get_consolidated_data(tax_filing_ins):
    return_dict = {"personalDetails":{}, "contactDetails":{}, "incomeDetails":{"otherIncomeDetails":[]}, "bankDetails":{}, "dependantDetails":list(), "spouseDetails":{}}

    #// Personal Details
    return_dict["personalDetails"]["userId"] = tax_filing_ins.user.id
    return_dict["personalDetails"]["firstName"]=tax_filing_ins.user.first_name
    return_dict["personalDetails"]["middleName"]= tax_filing_ins.user.middle_name 
    return_dict["personalDetails"]["lastName"]=tax_filing_ins.user.last_name
    return_dict["personalDetails"]["ssn"]= tax_filing_ins.user.ssn
    return_dict["personalDetails"]["dateOfBirth"]=  datetime.strftime(tax_filing_ins.user.dob, "%m/%d/%Y") if tax_filing_ins.user.dob else ""
    return_dict["personalDetails"]["gender"]= tax_filing_ins.user.gender
    return_dict["personalDetails"]["occupation"]= tax_filing_ins.user.job_title
    return_dict["personalDetails"]["residentialStatus"]= tax_filing_ins.user.residential_status
    return_dict["personalDetails"]["email"]= tax_filing_ins.user.email
    return_dict["personalDetails"]["taxPayerStatus"]= tax_filing_ins.user.status

    #// Contact Details
    if tax_filing_ins.user.contact:
        return_dict["contactDetails"]["street"]= tax_filing_ins.user.contact.street
        return_dict["contactDetails"]["apartment"]=tax_filing_ins.user.contact.apartment_no
        return_dict["contactDetails"]["city"]= tax_filing_ins.user.contact.city
        return_dict["contactDetails"]["state"]= tax_filing_ins.user.contact.state
        return_dict["contactDetails"]["zipCode"]= tax_filing_ins.user.contact.zip_code
        return_dict["contactDetails"]["country"]= tax_filing_ins.user.contact.country
        return_dict["contactDetails"]["primaryCountryCode"]= tax_filing_ins.user.contact.primary_number_country_code
        return_dict["contactDetails"]["primaryPhoneNumber"]= tax_filing_ins.user.contact.primary_number
        return_dict["contactDetails"]["secondaryCountryCode"]= tax_filing_ins.user.contact.secondary_number_country_code
        return_dict["contactDetails"]["secondaryPhoneNumber"]= tax_filing_ins.user.contact.secondary_number
        return_dict["contactDetails"]["contactEmail"]= tax_filing_ins.user.email
    else:
        return_dict["contactDetails"]["street"]= ""
        return_dict["contactDetails"]["apartment"]= ""
        return_dict["contactDetails"]["city"]= ""
        return_dict["contactDetails"]["state"]= ""
        return_dict["contactDetails"]["zipCode"]= ""
        return_dict["contactDetails"]["country"]= "USA"
        return_dict["contactDetails"]["primaryCountryCode"]= ""
        return_dict["contactDetails"]["primaryPhoneNumber"]= ""
        return_dict["contactDetails"]["secondaryCountryCode"]= ""
        return_dict["contactDetails"]["secondaryPhoneNumber"]= ""
        return_dict["contactDetails"]["contactEmail"]= tax_filing_ins.user.email

    #//Income Details
    if tax_filing_ins.income:
        return_dict["incomeDetails"]["interestIncome"]= tax_filing_ins.income.interest_income
        return_dict["incomeDetails"]["dividendIncome"]= tax_filing_ins.income.dividend_income
        return_dict["incomeDetails"]["soldStocks"]= tax_filing_ins.income.sold_stocks
        return_dict["incomeDetails"]["soldCrypto"]= tax_filing_ins.income.sold_cryptocurrency
        return_dict["incomeDetails"]["foreignIncome"]= tax_filing_ins.income.foreign_country_income
        return_dict["incomeDetails"]["retirementAccounts"]= tax_filing_ins.income.other_benefits
        return_dict["incomeDetails"]["stateTaxRefund"]= tax_filing_ins.income.last_year_state_tax_refunds
        return_dict["incomeDetails"]["foreignBankAccount"]= tax_filing_ins.income.foreign_banks_account_balance_exceeding_10000
        return_dict["incomeDetails"]["foreignAssets"]= tax_filing_ins.income.foreign_assets_value_exceeding_50000
        return_dict["incomeDetails"]["rentalIncome"]= tax_filing_ins.income.rental_income_in_usa
        return_dict["incomeDetails"]["income1099"]= tax_filing_ins.income.last_year_1099_misc_nec_income
        return_dict["incomeDetails"]["taxFiledLastYear"]= tax_filing_ins.income.filed_taxes_last_year
    else:
        return_dict["incomeDetails"]["interestIncome"]= False
        return_dict["incomeDetails"]["dividendIncome"]= False
        return_dict["incomeDetails"]["soldStocks"]= False
        return_dict["incomeDetails"]["soldCrypto"]= False
        return_dict["incomeDetails"]["foreignIncome"]= False
        return_dict["incomeDetails"]["retirementAccounts"]= False
        return_dict["incomeDetails"]["stateTaxRefund"]= False
        return_dict["incomeDetails"]["foreignBankAccount"]= False
        return_dict["incomeDetails"]["foreignAssets"]= False
        return_dict["incomeDetails"]["rentalIncome"]= False
        return_dict["incomeDetails"]["income1099"]= False
        return_dict["incomeDetails"]["taxFiledLastYear"]= False

    other_incomes = tax_filing_ins.other_incomes.all()
    for other_income in other_incomes:
        each_dict = dict()
        each_dict["id"] = other_income.id
        each_dict["incomeDescription"] = other_income.income_description
        each_dict["incomeAmount"] = other_income.income_amount

        return_dict["incomeDetails"]["otherIncomeDetails"].append(each_dict)

    #// additional Spouse Details (Initially hidden)
    if tax_filing_ins.user.status == "MARRIED":
        return_dict["spouseDetails"]["spouseFirstName"]= tax_filing_ins.user.spouse.first_name
        return_dict["spouseDetails"]["spouseMiddleInitial"]= tax_filing_ins.user.spouse.middle_name
        return_dict["spouseDetails"]["spouseLastName"]= tax_filing_ins.user.spouse.last_name
        return_dict["spouseDetails"]["spouseSsnOrItin"]= tax_filing_ins.user.spouse.ssn
        return_dict["spouseDetails"]["spouseApplyForItin"]=tax_filing_ins.user.spouse.apply_for_itin
        return_dict["spouseDetails"]["spouseDateOfBirth"]= datetime.strftime(tax_filing_ins.user.spouse.dob, "%m/%d/%Y")  if tax_filing_ins.user.spouse.dob else ""
        return_dict["spouseDetails"]["spouseGender"]= tax_filing_ins.user.spouse.gender
        return_dict["spouseDetails"]["spouseOccupation"]= tax_filing_ins.user.spouse.job_title
        return_dict["spouseDetails"]["spouseResidentialStatus"]= tax_filing_ins.user.spouse.residential_status
        return_dict["spouseDetails"]["spouseEmail"]= tax_filing_ins.user.spouse.email
    else:
        return_dict["spouseDetails"]["spouseFirstName"]= ""
        return_dict["spouseDetails"]["spouseMiddleInitial"]= ""
        return_dict["spouseDetails"]["spouseLastName"]= ""
        return_dict["spouseDetails"]["spouseSsnOrItin"]= ""
        return_dict["spouseDetails"]["spouseApplyForItin"]= False #// Default to False
        return_dict["spouseDetails"]["spouseDateOfBirth"]= ""
        return_dict["spouseDetails"]["spouseGender"]= ""
        return_dict["spouseDetails"]["spouseOccupation"]= ""
        return_dict["spouseDetails"]["spouseResidentialStatus"]= ""
        return_dict["spouseDetails"]["spouseEmail"]= ""

    if tax_filing_ins.dependants and len(list(tax_filing_ins.dependants.all())) > 0:
        return_dict["providedLivingSupport"] = True
    else:
        return_dict["providedLivingSupport"]= False

    dependants = tax_filing_ins.dependants.all()
    for dependant_ins in dependants:
        each_dict = dict()
        each_dict["id"] = dependant_ins.id
        each_dict["additionalFirstName"]= dependant_ins.first_name
        each_dict["additionalMiddleInitial"]= dependant_ins.middle_name
        each_dict["additionalLastName"]= dependant_ins.last_name
        each_dict["additionalSsnOrItin"]= dependant_ins.ssn
        each_dict["additionalApplyForItin"]= dependant_ins.apply_for_itin
        each_dict["additionalDateOfBirth"]= datetime.strftime(dependant_ins.dob, "%m/%d/%Y") if dependant_ins.dob else ""
        each_dict["additionalGender"]= dependant_ins.gender
        each_dict["additionalOccupation"]= dependant_ins.job_title
        each_dict["additionalVisaType"]= dependant_ins.visa_type
        each_dict["additionalEmail"]= dependant_ins.email
        each_dict["additionalRelationship"]= dependant_ins.relationship
        each_dict["additionalStayCount"]= dependant_ins.stay_period

        return_dict["dependantDetails"].append(each_dict)

    #//Bank Details
    if tax_filing_ins.bank:
        return_dict["bankDetails"]["bankingType"]= tax_filing_ins.refund_type
        return_dict["bankDetails"]["bankName"]= tax_filing_ins.bank.bank_name
        return_dict["bankDetails"]["accountHolderName"]= tax_filing_ins.bank.acc_holder_name
        return_dict["bankDetails"]["ownership"]= tax_filing_ins.bank.ownership
        return_dict["bankDetails"]["routingNumber"]= tax_filing_ins.bank.routing_number
        return_dict["bankDetails"]["confirmRoutingNumber"]= tax_filing_ins.bank.routing_number
        return_dict["bankDetails"]["accountNumber"]= tax_filing_ins.bank.account_number
        return_dict["bankDetails"]["confirmAccountNumber"]= tax_filing_ins.bank.account_number
        return_dict["bankDetails"]["accountType"]= tax_filing_ins.bank.account_type
        return_dict["bankDetails"]["confirmAccountType"]=tax_filing_ins.bank.account_type
    else:
        return_dict["bankDetails"]["bankingType"]= tax_filing_ins.refund_type if tax_filing_ins.refund_type else ""
        return_dict["bankDetails"]["bankName"]= ""
        return_dict["bankDetails"]["accountHolderName"]= ""
        return_dict["bankDetails"]["ownership"]= ""
        return_dict["bankDetails"]["routingNumber"]= ""
        return_dict["bankDetails"]["confirmRoutingNumber"]= ""
        return_dict["bankDetails"]["accountNumber"]= ""
        return_dict["bankDetails"]["confirmAccountNumber"]= ""
        return_dict["bankDetails"]["accountType"]= ""
        return_dict["bankDetails"]["confirmAccountType"]= ""
    
    for key, value in return_dict.items():
        if key in ["providedLivingSupport", "dependantDetails"]:
            continue
        for sub_key, sub_value in value.items():
            if (sub_value == None) and (not sub_value == False):
                return_dict[key][sub_key] = ''

    return_dict["id"] = tax_filing_ins.id
    
    return return_dict

def income_details_data(tax_filing_ins):
    return_dict = {"otherIncomeDetails":[]}
     #//Income Details
    if tax_filing_ins.income:
        return_dict["interestIncome"]= tax_filing_ins.income.interest_income
        return_dict["dividendIncome"]= tax_filing_ins.income.dividend_income
        return_dict["soldStocks"]= tax_filing_ins.income.sold_stocks
        return_dict["soldCrypto"]= tax_filing_ins.income.sold_cryptocurrency
        return_dict["foreignIncome"]= tax_filing_ins.income.foreign_country_income
        return_dict["retirementAccounts"]= tax_filing_ins.income.other_benefits
        return_dict["stateTaxRefund"]= tax_filing_ins.income.last_year_state_tax_refunds
        return_dict["foreignBankAccount"]= tax_filing_ins.income.foreign_banks_account_balance_exceeding_10000
        return_dict["foreignAssets"]= tax_filing_ins.income.foreign_assets_value_exceeding_50000
        return_dict["rentalIncome"]= tax_filing_ins.income.rental_income_in_usa
        return_dict["income1099"]= tax_filing_ins.income.last_year_1099_misc_nec_income
        return_dict["taxFiledLastYear"]= tax_filing_ins.income.filed_taxes_last_year
    else:
        return_dict["interestIncome"]= False
        return_dict["dividendIncome"]= False
        return_dict["soldStocks"]= False
        return_dict["soldCrypto"]= False
        return_dict["foreignIncome"]= False
        return_dict["retirementAccounts"]= False
        return_dict["stateTaxRefund"]= False
        return_dict["foreignBankAccount"]= False
        return_dict["foreignAssets"]= False
        return_dict["rentalIncome"]= False
        return_dict["income1099"]= False
        return_dict["taxFiledLastYear"]= False

    other_incomes = tax_filing_ins.other_incomes.all()
    for other_income in other_incomes:
        each_dict = dict()
        each_dict["id"] = other_income.id
        each_dict["incomeDescription"] = other_income.income_description
        each_dict["incomeAmount"] = other_income.income_amount

        return_dict["otherIncomeDetails"].append(each_dict)

    return return_dict