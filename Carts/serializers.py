from rest_framework import serializers

from Carts.models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta :
        model = CartItem
        fields = ('id', 'product', 'quantity')

    def validate(self, attrs):
        product = attrs['product']
        quantity = attrs['quantity']
        if not product.is_available:
            raise serializers.ValidationError("The product is not available")
        if quantity > product.stock:
            raise serializers.ValidationError("Quantity cannot be greater than the product stock")

        return attrs


    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        product = validated_data['product']
        quantity = validated_data['quantity']
        cart = getattr(user , 'cart', None)

        cart_item , created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            quantity=quantity)

        if not created :
            cart_item.quantity += quantity
            cart_item.save()

        return cart_item