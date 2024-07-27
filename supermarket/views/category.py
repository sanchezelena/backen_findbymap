from rest_framework import viewsets
from supermarket.models.category import Category
from supermarket.serializers.category import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer