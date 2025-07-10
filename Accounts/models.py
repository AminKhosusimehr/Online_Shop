from enum import unique

from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import GenderChoices

class User(AbstractUser) :
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="accounts_user_set",  # Unique related_name
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="accounts_user_set",  # Unique related_name
        related_query_name="user",
    )
    username = models.CharField(max_length=30,unique=True,blank=False,null=False)
    first_name = models.CharField(max_length=20 , blank=False , null=False )
    last_name = models.CharField(max_length=30 , blank=False , null=False)
    email = models.EmailField(unique=True, blank=True, null=True, default=None)
    phone_number = models.CharField(null=False,blank=False)
    address = models.TextField(blank=True,null=False)
    gender = models.CharField(choices=GenderChoices, blank=True, null=False)

    def __str__(self):
        return self.username