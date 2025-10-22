from django.core.validators import MinValueValidator
from django.db import models

from django.conf import settings
from rest_framework.exceptions import ValidationError

from Products.models import Product
from Utils.models import TimeStampedModel

from django.db.models import Sum , F


class UserCart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='user_cart')
    @property
    def total_price(self):
        total = CartItem.objects.filter(cart=self).aggregate(
            total=Sum(F('product__price') * F('quantity'))
        )['total']
        return total or 0

class CartItem(models.Model):
    cart = models.ForeignKey(UserCart, on_delete=models.CASCADE , related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)] , default=1)
