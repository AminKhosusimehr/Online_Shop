from django.shortcuts import render
from rest_framework import viewsets

import Carts


class CartViewSet(viewsets.ModelViewSet):
    class Meta :
        model = Carts

