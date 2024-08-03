from rest_framework import viewsets
from supermarket.models.rol import Rol
from supermarket.serializers.rol import RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer