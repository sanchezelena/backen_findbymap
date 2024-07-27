from rest_framework import serializers
from supermarket.models.ubication import Ubication

class UbicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubication
        fields = '__all__'
