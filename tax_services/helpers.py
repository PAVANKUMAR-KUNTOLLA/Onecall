from .models import *

def get_consolidated_data(id):
    return_dict = {"personalDetails":None, "contactDetails":None, "incomeDetails":None, "bankDetails":None, "dependantDetails":None, "spouseDetails":None}
    
    # #// Personal Details

    return_dict["firstName"]= "",
    return_dict["middleName"]= "",
    return_dict["lastName"]= "",
    return_dict["ssn"]= "",
    return_dict["dateOfBirth"]= "",
    return_dict["gender"]= "",
    return_dict["occupation"]= "",
    return_dict["residentialStatus"]= "",
    return_dict["email"]= "",

    #// Contact Details
    return_dict["street"]= "",
    return_dict["apartment"]= "",
    return_dict["city"]= "",
    return_dict["state"]= "",
    return_dict["zipCode"]= "",
    return_dict["country"]= "",
    return_dict["primaryCountryCode"]= "",
    return_dict["primaryPhoneNumber"]= "",
    return_dict["secondaryCountryCode"]= "",
    return_dict["secondaryPhoneNumber"]= "",
    return_dict["contactEmail"]= "",

    return_dict["taxFiledLastYear"]= "0", #// Set an initial value for taxFiledLastYear

    #// additional Spouse Details (Initially hidden)
    return_dict["taxPayerStatus"]= "1", #// Default to "No" (Single)
    return_dict["spouseFirstName"]= "",
    return_dict["spouseMiddleInitial"]= "",
    return_dict["spouseLastName"]= "",
    return_dict["spouseSsnOrItin"]= "",
    return_dict["applyForItin"]= "0", #// Default to "No"
    return_dict["spouseDateOfBirth"]= "",
    return_dict["spouseGender"]= "",
    return_dict["spouseOccupation"]= "",
    return_dict["spouseResidentialStatus"]= "",
    return_dict["spouseEmail"]= "",

    return_dict["providedLivingSupport"]= "1",
    return_dict["additionalFirstName"]= "",
    return_dict["additionalMiddleInitial"]= "",
    return_dict["additionalLastName"]= "",
    return_dict["additionalSsnOrItin"]= "",
    return_dict["applyForItin"]= "0", #// Default to "No"
    return_dict[" additionalDateOfBirth"]= "",
    return_dict["additionalGender"]= "",
    return_dict["additionalOccupation"]= "",
    return_dict["additionalResidentialStatus"]= "",
    return_dict["additionalEmail"]= "",

    #//Income Details
    return_dict["interestIncome"]= "no",
    return_dict["dividendIncome"]= "no",
    return_dict["soldStocks"]= "no",
    return_dict["soldCrypto"]= "no",
    return_dict["foreignIncome"]= "no",
    return_dict["retirementAccounts"]= "no",
    return_dict["stateTaxRefund"]= "no",
    return_dict["foreignBankAccount"]= "no",
    return_dict["foreignAssets"]= "no",
    return_dict["rentalIncome"]= "no",
    return_dict["income1099"]= "no",
    return_dict["incomeDescription"]= "",
    return_dict["incomeAmount"]= "",

    #//Bank Details

    return_dict["bankingType"]= "0",
    return_dict[" bankName"]= "",
    return_dict["accountHolderName"]= "",
    return_dict["ownership"]= "",
    return_dict["routingNumber"]= "",
    return_dict["confirmRoutingNumber"]= "",
    return_dict["accountNumber"]= "",
    return_dict["confirmAccountNumber"]= "",
    return_dict["accountType"]= "",
    return_dict["confirmAccountType"]= "",
    
    return return_dict