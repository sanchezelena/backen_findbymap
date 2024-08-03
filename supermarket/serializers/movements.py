from rest_framework import serializers
from supermarket.models.movements import Movements

class MovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movements
        fields = '__all__'