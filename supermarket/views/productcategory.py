from rest_framework import viewsets
from supermarket.models.productcategory import ProductCategory
from supermarket.serializers.productcategory import ProductCategorySerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer