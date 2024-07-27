from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentication.views.rol import RolViewSet
from authentication.views.user import AuthViewset

router = DefaultRouter()
router.register(r'router', RolViewSet)
router.register(r'auth', AuthViewset, basename='auth')

urlpatterns = [
    path('', include(router.urls))
]
