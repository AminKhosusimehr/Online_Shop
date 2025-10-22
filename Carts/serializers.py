from rest_framework import serializers

from Carts.models import CartItem
from Products.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ['id']

class PrductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id' , 'name']

class AllCartsSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='cart.user.username')
    product = PrductSerializer()
    class Meta :
        model = CartItem
        fields = ['user_name' , 'product' , 'quantity']
