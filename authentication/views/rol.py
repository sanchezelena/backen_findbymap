from rest_framework import viewsets
from authentication.models.rol import Rol
from authentication.serializers.rol import RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
