from rest_framework import viewsets
from supermarket.models.product import Product
from supermarket.serializers.product import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer