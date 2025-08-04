from django.core.validators import MinValueValidator
from django.db import models

from django.conf import settings
from rest_framework.exceptions import ValidationError

from Products.models import Product
from Utils.models import TimeStampedModel

class UserCart(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='user_cart')
    def __str__(self):
        return f'Cart {self.id} for {self.user.username}'

    @property
    def total_items_number(self):
        return sum(item.quantity for item in self.cart_items.all())
    @property
    def total_price(self):
        return sum(item.total_price for item in self.cart_items.select_related('product').all())
class CartItem(TimeStampedModel):
    cart = models.ForeignKey(UserCart,
                             on_delete=models.CASCADE,
                             related_name='cart_items')
    product = models.ForeignKey(Product,
                                on_delete=models.PROTECT,
                                related_name='cart_products')
    quantity = models.IntegerField(default=1,
                                   validators=[MinValueValidator(1)],)

    class Meta:
        unique_together = (('cart', 'product'),)
    def __str__(self):
        return f"{self.quantity} of  {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def clean(self):
        if hasattr(self.product , 'is_available' ) and not self.product.is_available :
            raise ValidationError("The product is not available")
        if hasattr(self.product , 'stock') and self.quantity > self.product.stock :
            raise ValidationError(f"Requested quantity ({self.quantity}) exceeds stock ({self.product.stock}) for {self.product.name}.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)