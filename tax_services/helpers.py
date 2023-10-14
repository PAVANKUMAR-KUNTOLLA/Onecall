from .models import *

def get_consolidated_data(id):
    return_dict = {"personalDetails":{}, "contactDetails":{}, "incomeDetails":{}, "bankDetails":{}, "dependantDetails":{}, "spouseDetails":{}}
    tax_filing_ins = TaxFiling.objects.get(id=id)
    return_dict["id"] = tax_filing_ins.id

    #// Personal Details
    return_dict["personalDetails"]["userId"] = tax_filing_ins.user.id
    return_dict["personalDetails"]["firstName"]=tax_filing_ins.user.first_name
    return_dict["personalDetails"]["middleName"]= tax_filing_ins.user.middle_name 
    return_dict["personalDetails"]["lastName"]=tax_filing_ins.user.last_name
    return_dict["personalDetails"]["ssn"]= tax_filing_ins.user.ssn
    return_dict["personalDetails"]["dateOfBirth"]= tax_filing_ins.user.dob
    return_dict["personalDetails"]["gender"]= tax_filing_ins.user.gender
    return_dict["personalDetails"]["occupation"]= tax_filing_ins.user.job_title
    return_dict["personalDetails"]["residentialStatus"]= tax_filing_ins.user.residental_status
    return_dict["personalDetails"]["email"]= tax_filing_ins.user.email

    #// Contact Details
    if tax_filing_ins.user.contact:
        return_dict["street"]= tax_filing_ins.user.contact.street
        return_dict["apartment"]=tax_filing_ins.user.contact.apartment_no
        return_dict["city"]= tax_filing_ins.user.contact.city
        return_dict["state"]= tax_filing_ins.user.contact.state
        return_dict["zipCode"]= tax_filing_ins.user.contact.zip_code
        return_dict["country"]= tax_filing_ins.user.contact.country
        return_dict["primaryCountryCode"]= tax_filing_ins.user.contact.primary_number_country_code
        return_dict["primaryPhoneNumber"]= tax_filing_ins.user.contact.primary_number
        return_dict["secondaryCountryCode"]= tax_filing_ins.user.contact.secondary_number_country_code
        return_dict["secondaryPhoneNumber"]= tax_filing_ins.user.contact.secondary_number
        return_dict["contactEmail"]= tax_filing_ins.user.email
    else:
        return_dict["street"]= ""
        return_dict["apartment"]= ""
        return_dict["city"]= ""
        return_dict["state"]= ""
        return_dict["zipCode"]= ""
        return_dict["country"]= ""
        return_dict["primaryCountryCode"]= ""
        return_dict["primaryPhoneNumber"]= ""
        return_dict["secondaryCountryCode"]= ""
        return_dict["secondaryPhoneNumber"]= ""
        return_dict["contactEmail"]= ""

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
        return_dict["incomeDescription"]=tax_filing_ins.income.income_description
        return_dict["incomeAmount"]= tax_filing_ins.income.income_amount
        return_dict["taxFiledLastYear"]= tax_filing_ins.income.filed_taxes_last_year
    else:
        return_dict["interestIncome"]= "no"
        return_dict["dividendIncome"]= "no"
        return_dict["soldStocks"]= "no"
        return_dict["soldCrypto"]= "no"
        return_dict["foreignIncome"]= "no"
        return_dict["retirementAccounts"]= "no"
        return_dict["stateTaxRefund"]= "no"
        return_dict["foreignBankAccount"]= "no"
        return_dict["foreignAssets"]= "no"
        return_dict["rentalIncome"]= "no"
        return_dict["income1099"]= "no"
        return_dict["incomeDescription"]= ""
        return_dict["incomeAmount"]= ""
        return_dict["taxFiledLastYear"]= "0"

    #// additional Spouse Details (Initially hidden)
    if tax_filing_ins.user.status == "MARRIED":
        return_dict["taxPayerStatus"]= tax_filing_ins.user.status
        return_dict["spouseFirstName"]= tax_filing_ins.user.spouse.first_name
        return_dict["spouseMiddleInitial"]= tax_filing_ins.user.spouse.middle_name
        return_dict["spouseLastName"]= tax_filing_ins.user.spouse.last_name
        return_dict["spouseSsnOrItin"]= tax_filing_ins.user.spouse.ssn
        return_dict["applyForItin"]= False
        return_dict["spouseDateOfBirth"]= tax_filing_ins.user.spouse.dob
        return_dict["spouseGender"]= tax_filing_ins.user.spouse.gender
        return_dict["spouseOccupation"]= tax_filing_ins.user.spouse.job_title
        return_dict["spouseResidentialStatus"]= tax_filing_ins.user.spouse.status
        return_dict["spouseEmail"]= tax_filing_ins.user.spouse.email
    else:
        return_dict["taxPayerStatus"]= "SINGLE"
        return_dict["spouseFirstName"]= ""
        return_dict["spouseMiddleInitial"]= ""
        return_dict["spouseLastName"]= ""
        return_dict["spouseSsnOrItin"]= ""
        return_dict["applyForItin"]= "0" #// Default to "No"
        return_dict["spouseDateOfBirth"]= ""
        return_dict["spouseGender"]= ""
        return_dict["spouseOccupation"]= ""
        return_dict["spouseResidentialStatus"]= ""
        return_dict["spouseEmail"]= ""

    if tax_filing_ins.dependants:
        dependants = tax_filing_ins.dependants.all()
        for dependant_ins in dependants:
            return_dict["providedLivingSupport"]= True
            return_dict["additionalFirstName"]= dependant_ins.first_name
            return_dict["additionalMiddleInitial"]= dependant_ins.middle_name
            return_dict["additionalLastName"]= dependant_ins.last_name
            return_dict["additionalSsnOrItin"]= dependant_ins.ssn
            return_dict["applyForItin"]= False
            return_dict[" additionalDateOfBirth"]= dependant_ins.dob
            return_dict["additionalGender"]= ""
            return_dict["additionalOccupation"]= ""
            return_dict["additionalResidentialStatus"]= ""
            return_dict["additionalEmail"]= ""
    else:
        return_dict["providedLivingSupport"]= False
        return_dict["additionalFirstName"]= ""
        return_dict["additionalMiddleInitial"]= ""
        return_dict["additionalLastName"]= ""
        return_dict["additionalSsnOrItin"]= ""
        return_dict["applyForItin"]= "0" #// Default to "No"
        return_dict[" additionalDateOfBirth"]= ""
        return_dict["additionalGender"]= ""
        return_dict["additionalOccupation"]= ""
        return_dict["additionalResidentialStatus"]= ""
        return_dict["additionalEmail"]= ""
    
    #//Bank Details
    if tax_filing_ins.bank:
        return_dict["bankingType"]= tax_filing_ins.bank.service_type
        return_dict[" bankName"]= tax_filing_ins.bank.name
        return_dict["accountHolderName"]= tax_filing_ins.bank.acc_holder_name
        return_dict["ownership"]= tax_filing_ins.bank.ownership
        return_dict["routingNumber"]= tax_filing_ins.routing_number
        return_dict["confirmRoutingNumber"]= tax_filing_ins.routing_number
        return_dict["accountNumber"]= tax_filing_ins.bank.account_number
        return_dict["confirmAccountNumber"]= tax_filing_ins.bank.acc_holder_name
        return_dict["accountType"]= tax_filing_ins.bank.account_type
        return_dict["confirmAccountType"]=tax_filing_ins.bank.account_type
    else:
        return_dict["bankingType"]= ""
        return_dict[" bankName"]= ""
        return_dict["accountHolderName"]= ""
        return_dict["ownership"]= ""
        return_dict["routingNumber"]= ""
        return_dict["confirmRoutingNumber"]= ""
        return_dict["accountNumber"]= ""
        return_dict["confirmAccountNumber"]= ""
        return_dict["accountType"]= ""
        return_dict["confirmAccountType"]= ""
    
    return return_dict