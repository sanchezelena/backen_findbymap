
from rest_framework import viewsets
from supermarket.models.movements import Movements
from supermarket.serializers.movements import MovementsSerializer

class MovementsViewSet(viewsets.ModelViewSet):
    queryset = Movements.objects.all()
    serializer_class = MovementsSerializer