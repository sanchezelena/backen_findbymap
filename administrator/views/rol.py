from rest_framework import viewsets
from administrator.models.rol import Rol
from administrator.serializers.rol import RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer