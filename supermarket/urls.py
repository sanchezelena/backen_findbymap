from django.urls import path, include
from rest_framework.routers import DefaultRouter
from supermarket.views.category import CategoryViewSet
from supermarket.views.product import ProductViewSet
from supermarket.views.ubication import UbicationViewSet
from supermarket.views.productcategory import ProductCategoryViewSet
from administrator.views.rol import RolViewSet
from supermarket.views.dare import DareViewSet
from supermarket.views.movements import MovementsViewSet
from supermarket.views.map import generate_route_image

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'ubications', UbicationViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'roles', RolViewSet)
router.register(r'dares', DareViewSet)
router.register(r'movements', MovementsViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('generate-route-image/<int:product_id>/', generate_route_image),
]

