from django.db import models
import datetime
from crum import get_current_user
from users.models import GENDER_CHOICES

VISA_TYPE_CHOICES = [("H4", "H4"), ("US Citizen", "US Citizen"), ("L2", "L2"), ("Green Card", "Green Card"), ("Other", "Other")]
REFUND_CHOICES = [("DIRECT DEPOSIT INTO MY BANK ACCOUNT", "DIRECT DEPOSIT INTO MY BANK ACCOUNT"), ("PAPER CHECK", "PAPER CHECK")]
OWNERSHIP_CHOICES = [("TAXPAYER/SPOUSE", "TAXPAYER/SPOUSE"), ("JOINT", "JOINT")]
BANK_ACCOUNT_TYPE = [("SAVINGS", "SAVINGS"), ("CHECKING", "CHECKING")]
APPOINTMENT_STATUS_CHOICES = [("BOOKED", "BOOKED"), ("COMPLETED", "COMPLETED"), ("CANCELLED", "CANCELLED")]
PAYMENT_MODES = [("INTERNET BANKING", "INTERNET BANKING"), ("CREDIT/DEBIT CARD", ("CREDIT/DEBIT CARD")), ("PAYPAL", "PAYPAL")]
PAYMENT_STATUS_CHOICES = [("INITIATED", "INITIATED"),("PROCESSED", "PROCESSED"),  ("SUCCESS", "SUCCESS"), ("FAILED", "FAILED")]
FILING_STATUS_CHOICES = [("INITIATED", "INITIATED"),("IN_PROGRESS", "IN-PROGRESS"), ("COMPLETED", "COMPLETED")]
SERVICE_TYPE_CHOICES = [("REGULAR", "REGULAR")]

# Create your models here.

class FinancialYear(models.Model):
    name = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', on_delete=models.RESTRICT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.created_by = user

        super(FinancialYear, self).save(*args, **kwargs)

class Income(models.Model):
    filing = models.ForeignKey("tax_services.TaxFiling", on_delete=models.CASCADE, null=True, blank=True, related_name="filer_income_details")
    filed_taxes_last_year = models.BooleanField(default=False)
    interest_income = models.BooleanField(default=False)
    dividend_income = models.BooleanField(default=False)
    sold_stocks = models.BooleanField(default=False)
    sold_cryptocurrency = models.BooleanField(default=False)
    foreign_country_income = models.BooleanField(default=False)
    other_benefits = models.BooleanField(default=False)
    last_year_state_tax_refunds = models.BooleanField(default=False)
    foreign_banks_account_balance_exceeding_10000 = models.BooleanField(default=False)
    foreign_assets_value_exceeding_50000 = models.BooleanField(default=False)
    rental_income_in_usa = models.BooleanField(default=False)
    last_year_1099_misc_nec_income = models.BooleanField(default=False)
    income_description = models.TextField(null=True, blank=True)
    income_amount = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', on_delete=models.RESTRICT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'Income Details of {self.filing.user.email} for year {self.filing.year.start_date.strftime("%Y")}'

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.created_by = user

        super(Income, self).save(*args, **kwargs)

class Dependant(models.Model):
    filing = models.ForeignKey("tax_services.TaxFiling", on_delete=models.CASCADE, null=True, blank=True, related_name="filer_dependants")
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    relationship = models.CharField(max_length=255)
    country_of_stay = models.CharField(max_length=255, null=True, blank=True)
    stay_period = models.IntegerField(default=0)
    visa_type = models.CharField(max_length=255, choices=VISA_TYPE_CHOICES)
    ssn = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    apply_for_itin = models.BooleanField(default=False)
    job_title = models.CharField(max_length=555, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', on_delete=models.RESTRICT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.email}'

    @property
    def name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.created_by = user

        super(Dependant, self).save(*args, **kwargs)

class Bank(models.Model):
    filing = models.ForeignKey("tax_services.TaxFiling", on_delete=models.CASCADE, null=True, blank=True, related_name="filer_tax_refund_account")
    bank_name = models.CharField(max_length=555, null=True, blank=True)
    acc_holder_name = models.CharField(max_length=555, null=True, blank=True)
    ownership = models.CharField(max_length=255, choices=OWNERSHIP_CHOICES)
    routing_number = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    account_type = models.CharField(max_length=255, null=True, blank=True, choices=BANK_ACCOUNT_TYPE)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', on_delete=models.RESTRICT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'Bank Account Details of {self.filing.user.email} for year {self.filing.year.start_date.strftime("%Y")}'

    @property
    def name(self):
        return f'{self.bank_name}'

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.created_by = user

        super(Bank, self).save(*args, **kwargs)

def get_file_path(instance, filename):
    return f'TaxDocs/U{instance.id}_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}_{filename}'

class Appointment(models.Model):
    filing = models.ForeignKey("tax_services.TaxFiling", on_delete=models.CASCADE, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_zone = models.CharField(max_length=255, default="CST")
    status = models.CharField(max_length=255, choices=APPOINTMENT_STATUS_CHOICES, default="BOOKED")

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', on_delete=models.RESTRICT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'Appointment for {self.filing.user.email} on {self.start_time.strftime("%Y-%m-%d")}'

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.created_by = user

        super(Appointment, self).save(*args, **kwargs)

class Payment(models.Model):
    filing = models.ForeignKey("tax_services.TaxFiling", on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    mode_of_payment = models.CharField(max_length=255, choices=PAYMENT_MODES)
    card_number = models.CharField(max_length=255, null=True, blank=True)
    exp_date = models.DateField(null=True, blank=True)
    cvv = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    street_address = models.CharField(max_length=555, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=PAYMENT_STATUS_CHOICES, default="INITIATED")

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', on_delete=models.RESTRICT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'Payment Details of {self.filing.name} for year {self.filing.year.start_date.strftime("%Y")}'

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.created_by = user

        super(Payment, self).save(*args, **kwargs)

def get_tax_returns_file_path(instance, filename):
    return f'TaxReturns/U{instance.filing.user.id}_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}_{filename}'

class TaxReturns(models.Model):
    filing = models.ForeignKey("tax_services.TaxFiling", on_delete=models.CASCADE, null=True, blank=True)
    file_name = models.FileField(null=True, blank=True, upload_to=get_tax_returns_file_path)
    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = "Tax Returns"
    
    def __str__(self):
        return f'Tax Returns of {self.filing.user.email} for Year {self.filing.year}'

class TaxFiling(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    year = models.ForeignKey("tax_services.FinancialYear", on_delete=models.CASCADE)
    service_type = models.CharField(max_length=255, choices=SERVICE_TYPE_CHOICES, default="REGULAR")
    income = models.ForeignKey("tax_services.Income", on_delete=models.CASCADE, null=True, blank=True)
    dependants = models.ManyToManyField("tax_services.Dependant")
    refund_type = models.CharField(max_length=255, choices=REFUND_CHOICES, null=True, blank=True)
    bank = models.ForeignKey("tax_services.Bank", on_delete=models.CASCADE, null=True, blank=True)
    tax_docs = models.FileField(null=True, blank=True, upload_to=get_file_path)
    tax_returns = models.ManyToManyField("tax_services.TaxReturns")
    appointments = models.ManyToManyField("tax_services.Appointment")
    payments = models.ManyToManyField("tax_services.Payment")
    status = models.CharField(max_length=255, choices=FILING_STATUS_CHOICES, default="INITIATED")

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = "Tax Filing"
        unique_together = ['user', 'year']
    
    def __str__(self):
        return f'Tax Filing of {self.user.email} for Year {self.year}'

    def save(self, *args, **kwargs):
        user = get_current_user()

        super(TaxFiling, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        user = get_current_user()

        if not (user.is_admin or user.is_client and user.id == self.user.id):
            raise Exception("UnAuthorized")
        super(TaxFiling, self).save(*args, **kwargs)

class Referal(models.Model):
    referred_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.referred_by.email

    def save(self, *args, **kwargs):
        user = get_current_user()

        super(Referal, self).save(*args, **kwargs)
