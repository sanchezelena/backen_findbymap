from rest_framework import viewsets
from supermarket.models.ubication import Ubication
from supermarket.serializers.ubication import UbicationSerializer

class UbicationViewSet(viewsets.ModelViewSet):
    queryset = Ubication.objects.all()
    serializer_class = UbicationSerializer