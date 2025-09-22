from itertools import product
from pickle import FALSE

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions

import Carts
from Carts.models import CartItem , UserCart
from Carts.serializers import CartItemSerializer
from Products.models import Product

class CartsViewSet(viewsets.ViewSet):
    serializer_class = CartItemSerializer

    @action(detail=False , methods=['POST'])
    def add_to_cart(self, request):
        user = request.user
        cart = UserCart.objects.get(user=user)
        product_id = request.data['product']
        product = Product.objects.get(id=product_id)
        quantity = request.data['quantity']
        CartItem.objects.create(cart=cart , product=product , quantity=quantity)
        return Response('Item added' , status=status.HTTP_201_CREATED)
