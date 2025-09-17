from rest_framework import serializers

from Products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id',)

    def validate(self, data):
        is_available = data['is_available']
        stock = data['stock']

        if not is_available and stock > 0 :
            raise serializers.ValidationError("The stock must be zero for an unavailable product")
        return data