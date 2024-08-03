from django.urls import path, include
from rest_framework.routers import DefaultRouter
from supermarket.views.category import CategoryViewSet
from supermarket.views.product import ProductViewSet
from supermarket.views.ubication import UbicationViewSet
from supermarket.views.productcategory import ProductCategoryViewSet
from administrator.views.employee import EmployeeAdminViewSet
from administrator.views.rol import RolViewSet
from supermarket.views.dare import DareViewSet
from supermarket.views.movements import MovementsViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'ubications', UbicationViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'employees', EmployeeAdminViewSet)
router.register(r'roles', RolViewSet)
router.register(r'dares', DareViewSet)
router.register(r'movements', MovementsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

