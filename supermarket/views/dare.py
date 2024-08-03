from rest_framework import viewsets
from supermarket.models.dare import Dare
from supermarket.serializers.dare import DareSerializer

class DareViewSet(viewsets.ModelViewSet):
    queryset = Dare.objects.all()
    serializer_class = DareSerializer