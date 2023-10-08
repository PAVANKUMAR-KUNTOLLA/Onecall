from django.db import models
from crum import get_current_user
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from rest_framework.authtoken.models import Token

# Create your models here.

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
    name = models.CharField(max_length=255, null=True, blank=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    referred_by = models.ForeignKey("self", on_delete=models.RESTRICT, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    account_terminated = models.BooleanField(default=False, editable=False)

    objects = UserManager()
    
    def __str__(self):
        return self.email

    @property
    def referral_id(self):
        return f'OCTS{self.id}'

    def users_return(self):
        return User.objects.filter(account_terminated=False)

    def save(self, *args, **kwargs):
       
        if not self.is_active:
            token_ins = Token.objects.filter(user_id=self.id)
            if token_ins:
                token_ins.delete()

        super(User, self).save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     self.account_terminated = True
    #     self.is_active = False
    #     super(User, self).save(*args, **kwargs)