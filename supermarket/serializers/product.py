from rest_framework import serializers
from supermarket.models.product import Product
from supermarket.serializers.category import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'