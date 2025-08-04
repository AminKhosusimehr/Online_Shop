
from django.db import models

from Accounts.models import User
from Products.models import Product


class UserCart(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

