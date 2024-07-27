from django.urls import path, include
from rest_framework.routers import DefaultRouter
from supermarket.views.category import CategoryViewSet
from supermarket.views.product import ProductViewSet
from supermarket.views.ubication import UbicationViewSet
from supermarket.views.productcategory import ProductCategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'ubications', UbicationViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-categories', ProductCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

