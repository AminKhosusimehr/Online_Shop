from django.shortcuts import render
from rest_framework import viewsets, permissions

import Carts
from Carts.models import CartItem
from Carts.serializers import CartItemSerializer


class CartItemViewSet(viewsets.ModelViewSet):
        serializer_class = CartItemSerializer
        permission_classes = [permissions.IsAuthenticated]

        def get_queryset(self):
                return CartItem.objects.filter(cart=self.request.user.cart_items)

        def perform_create(self, serializer):
                user = self.request.user
                cart = getattr(user , 'cart_items', None)
                serializer.save(cart=cart)