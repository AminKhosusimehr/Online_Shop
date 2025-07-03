from enum import unique

from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import gender_choices

class User(AbstractUser) :
    username = models.CharField(max_length=30,unique=True,blank=False,null=False)
    first_name = models.CharField(max_length=20 , blank=False , null=False )
    last_name = models.CharField(max_length=30 , blank=False , null=False)
    email = models.EmailField(blank=True,null=True)
    phone_number = models.CharField(null=False,blank=False)
    address = models.TextField(blank=True,null=False)
    gender = models.CharField(choices=gender_choices,blnak=True,null=False)


