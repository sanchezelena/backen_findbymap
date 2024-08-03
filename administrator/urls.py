from django.urls import path, include
from rest_framework.routers import DefaultRouter
from administrator.views.employee import EmployeeViewSet
from administrator.views.rol import RolViewSet


router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'roles', RolViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
