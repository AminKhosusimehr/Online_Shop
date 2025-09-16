from django.contrib import admin
from Carts.models import UserCart , CartItem

admin.site.register(CartItem)
admin.site.register(UserCart)
