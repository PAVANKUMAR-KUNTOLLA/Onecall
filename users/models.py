from django.db import models
from crum import get_current_user
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from rest_framework.authtoken.models import Token

# Create your models here.

ROLE_CHOICES = [("CLIENT", "CLIENT"), ("ADMIN", "ADMIN"), ("CUSTOMER SERVICE", "CUSTOMER_SERVICE")]
GENDER_CHOICES=[("MALE", "MALE"), ("FEMALE", "FEMALE"), ("Other", "Other")]
residential_STATUS_CHOICES = [("VISA", "VISA"), ("CITIZENSHIP", "CITIZENSHIP")]
MARITAL_CHOICES = [("SINGLE", "SINGLE"), ("MARRIED", "MARRIED")]

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

    def create_superuser(self, email, password, first_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', "ADMIN")
        extra_fields.setdefault('gender', "MALE")

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    ssn = models.CharField(unique=True, max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    job_title = models.CharField(max_length=555, null=True, blank=True)
    residential_status = models.CharField(max_length=255, choices=residential_STATUS_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=255, choices=MARITAL_CHOICES, null=True, blank=True)
    spouse = models.ForeignKey("users.User", on_delete=models.RESTRICT, null=True, blank=True, related_name="partner")
    contact = models.ForeignKey("users.Contact", on_delete=models.CASCADE, blank=True, null=True, related_name="contact_info")
    tax_filings = models.ManyToManyField("tax_services.TaxFiling", related_name="filings")
    apply_for_itin = models.BooleanField(default=False)
    referred_by = models.ForeignKey("self", on_delete=models.RESTRICT, null=True, blank=True, editable=False)
    
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
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
        return self.user.email

    def save(self, *args, **kwargs):
        user = get_current_user()
        super(Contact, self).save(*args, **kwargs)