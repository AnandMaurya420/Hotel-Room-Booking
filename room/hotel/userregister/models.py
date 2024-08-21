from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager 

# Create your models here.

class Usermanager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):  
 
        if not email:  
            raise ValueError(('The Email must be Required'))  
        email = self.normalize_email(email)  
          
        user = self.model(email=email, **extra_fields)  
        user.set_password(password)  
        user.save(using=self._db)
        return user 
                                              
    
    def create_superuser(self, email, password, **extra_fields): 
        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)  
        extra_fields.setdefault('is_active', True) 

        if extra_fields.get('is_staff') is not True:  
            raise ValueError(('Superuser must have is_staff=True.'))
        
        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractUser):

    username = models.CharField(unique=True,max_length=20)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    is_email_verified = models.BooleanField(default=False)
    is_mobile_verified = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=6, null=True, blank=True)
    mobile_otp = models.CharField(max_length=6, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = Usermanager()  

    def __str__(self) :
        return self.email

