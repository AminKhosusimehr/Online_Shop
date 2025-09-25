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

    @action(detail=False , methods=['POST'] , permission_classes=[permissions.IsAuthenticated])
    def add_to_cart(self, request):
        user = request.user
        cart = UserCart.objects.get(user=user)
        product_id = request.data['product']
        product = Product.objects.get(id=product_id)
        quantity = int(request.data['quantity'])
        try:
            cart_item = CartItem.objects.get(cart=cart , product = product )
            cart_item.quantity = cart_item.quantity + quantity
            cart_item.save()
            return Response("Quantity updated " , status=status.HTTP_200_OK)


        except CartItem.DoesNotExist:
            CartItem.objects.create(cart=cart, product=product, quantity=quantity)
            return Response('Item added', status=status.HTTP_201_CREATED)


