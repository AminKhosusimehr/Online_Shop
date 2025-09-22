from django.core.validators import MinValueValidator
from django.db import models

from django.conf import settings
from rest_framework.exceptions import ValidationError

from Products.models import Product
from Utils.models import TimeStampedModel

class UserCart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(UserCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)] , default=1)
