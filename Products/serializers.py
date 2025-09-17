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

    def validate_name(self, name):
        current_instance = getattr(self, 'instance', None)
        existing_products = Product.objects.filter(name__iexact=name)
        if current_instance:
            existing_products = existing_products.exclude(id=current_instance.id)
        if existing_products.exists():
            raise serializers.ValidationError("The product with this name already exists")

        return name