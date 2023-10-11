from django.db import models
from crum import get_current_user
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from rest_framework.authtoken.models import Token

# Create your models here.

ROLE_CHOICES = [("CLIENT", "CLIENT"), ("ADMIN", "ADMIN"), ("CUSTOMER SERVICE", "CUSTOMER_SERVICE")]
GENDER_CHOICES=[("MALE", "MALE"), ("FEMALE", "FEMALE"), ("Other", "Other")]
RESIDENTAL_STATUS_CHOICES = [("VISA", "VISA"), ("CITIZENSHIP", "CITIZENSHIP")]
VISA_TYPE_CHOICES = [("H4", "H4"), ("US Citizen", "US Citizen"), ("L2", "L2"), ("Green Card", "Green Card"), ("Other", "Other")]
MARITAL_CHOICES = [("SINGLE", "SINGLE"), ("MARRIED", "MARRIED")]
REFUND_CHOICES = [("DIRECT DEPOSIT INTO MY BANK ACCOUNT", "DIRECT DEPOSIT INTO MY BANK ACCOUNT"), ("PAPER CHECK", "PAPER CHECK")]
OWNERSHIP_CHOICES = [("TAXPAYER/SPOUSE", "TAXPAYER/SPOUSE"), ("JOINT", "JOINT")]
BANK_ACCOUNT_TYPE = [("SAVINGS", "SAVINGS"), ("CHECKING", "CHECKING")]
APPOINTMENT_STATUS_CHOICES = [("BOOKED", "BOOKED"), ("COMPLETED", "COMPLETED"), ("CANCELLED", "CANCELLED")]
PAYMENT_MODES = [("INTERNET BANKING", "INTERNET BANKING"), ("CREDIT/DEBIT CARD", ("CREDIT/DEBIT CARD")), ("PAYPAL", "PAYPAL")]
PAYMENT_STATUS_CHOICES = [("INITIATED", "INITIATED"),("PROCESSED", "PROCESSED"),  ("SUCCESS", "SUCCESS"), ("FAILED", "FAILED")]
FILING_STATUS_CHOICES = [("INITIATED", "INITIATED"),("IN_PROGRESS", "IN-PROGRESS"), ("COMPLETED", "COMPLETED")]

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email for user must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    ssn = models.CharField(unique=True, max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    job_title = models.CharField(max_length=555, null=True, blank=True)
    residental_status = models.CharField(max_length=255, choices=RESIDENTAL_STATUS_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=255, choices=MARITAL_CHOICES, null=True, blank=True)
    spouse = models.ForeignKey("users.User", on_delete=models.RESTRICT, null=True, blank=True, related_name="partner")
    contact = models.ForeignKey("users.Contact", on_delete=models.CASCADE, blank=True, null=True, related_name="contact_info")
    tax_filings = models.ManyToManyField("users.TaxFiling", related_name="filings")
    referred_by = models.ForeignKey("self", on_delete=models.RESTRICT, null=True, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    account_terminated = models.BooleanField(default=False, editable=False)

    objects = UserManager()
    
    def __str__(self):
        return self.email

    @property
    def referral_id(self):
        return f'OCTS{self.id}'

    @property
    def is_client(self):
        if self.role == "CLIENT":
            return True
        else:
            return False

    @property
    def is_admin(self):
        if self.role == "ADMIN":
            return True
        else:
            return False

    @property
    def is_customer_service(self):
        if self.role == "CUSTOMER_SERVICE":
            return True 
        else:
            return False

    @property
    def name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def users_return(self):
        return User.objects.filter(account_terminated=False)

    def save(self, *args, **kwargs):
       
        if not self.is_active:
            token_ins = Token.objects.filter(user_id=self.id)
            if token_ins:
                token_ins.delete()

        super(User, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # self.account_terminated = True
        self.is_active = False
        super(User, self).save(*args, **kwargs)


class Contact(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_contact")
    street	= models.CharField(max_length=555)																								
    apartment_no = models.CharField(max_length=555, null=True, blank=True)																	
    city =  models.CharField(max_length=555)																										
    state =  models.CharField(max_length=255)																										
    zip_code =  models.CharField(max_length=255)																										
    country	=  models.CharField(max_length=255, null=True, blank=True)
    primary_number_country_code = models.CharField(max_length=255)																							
    primary_number = models.CharField(max_length=255)							
    secondary_number_country_code = models.CharField(max_length=255, null=True, blank=True)																							
    secondary_number = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        user = get_current_user()
        super(Contact, self).save(*args, **kwargs)

class FinancialYear(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', on_delete=models.RESTRICT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        self.name

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.created_by = user

        super(FinancialYear, self).save(*args, **kwargs)

class Income(models.Model):
    filing = models.ForeignKey("users.TaxFiling", on_delete=models.CASCADE, null=True, blank=True, related_name="filer_income_details")
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
        return f'Income Details of {self.filing.name} for year {self.filing.year.start_date.strftime("%Y")}'

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.created_by = user

        super(Income, self).save(*args, **kwargs)

class Dependant(models.Model):
    filing = models.ForeignKey("users.TaxFiling", on_delete=models.CASCADE, null=True, blank=True, related_name="filer_dependants")
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    relationship = models.CharField(max_length=255)
    country_of_stay = models.CharField(max_length=255)
    stay_period = models.IntegerField(default=0)
    visa_type = models.CharField(max_length=255, choices=VISA_TYPE_CHOICES)
    ssn = models.CharField(max_length=255, null=True, blank=True)
    itin = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', on_delete=models.RESTRICT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    @property
    def name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.created_by = user

        super(Dependant, self).save(*args, **kwargs)

class Bank(models.Model):
    filing = models.ForeignKey("users.TaxFiling", on_delete=models.CASCADE, null=True, blank=True, related_name="filer_tax_refund_account")
    name = models.CharField(max_length=555, null=True, blank=True)
    acc_holder_name = models.CharField(max_length=555, null=True, blank=True)
    ownership = models.CharField(max_length=255, choices=OWNERSHIP_CHOICES)
    routing_number = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    account_type = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', on_delete=models.RESTRICT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'Bank Account Details of {self.filing.name} for year {self.filing.year.start_date.strftime("%Y")}'

    @property
    def name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.created_by = user

        super(Bank, self).save(*args, **kwargs)

def get_file_path(instance, filename):
    return f'TaxDocs/{instance.id}_{filename}'

class Appointment(models.Model):
    filing = models.ForeignKey("users.TaxFiling", on_delete=models.CASCADE, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_zone = models.CharField(max_length=255, default="CST")
    status = models.CharField(max_length=255, choices=APPOINTMENT_STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', on_delete=models.RESTRICT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'Appointment for {self.filing.name} on {start_time.strftime("%Y-%m-%d")}'

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.created_by = user

        super(Appointment, self).save(*args, **kwargs)

class Payment(models.Model):
    filing = models.ForeignKey("users.TaxFiling", on_delete=models.CASCADE, null=True, blank=True)
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
    status = models.CharField(max_length=255, choices=PAYMENT_STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', on_delete=models.RESTRICT, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'Payment Details of {self.filing.name} for year {self.filing.year.start_date.strftime("%Y")}'

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.created_by = user

        super(Payment, self).save(*args, **kwargs)

class TaxFiling(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    year = models.ForeignKey("users.FinancialYear", on_delete=models.CASCADE)
    income = models.ForeignKey("users.Income", on_delete=models.CASCADE, null=True, blank=True)
    dependants = models.ManyToManyField("users.Dependant")
    refund_type = models.CharField(max_length=255, choices=REFUND_CHOICES, null=True, blank=True)
    bank = models.ForeignKey("users.Bank", on_delete=models.CASCADE, null=True, blank=True)
    tax_docs = models.FileField(null=True, blank=True, upload_to=get_file_path)
    appointments = models.ManyToManyField("users.Appointment")
    payments = models.ManyToManyField("users.Payment")
    status = models.CharField(max_length=255, choices=FILING_STATUS_CHOICES, default="INITIATED")

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
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