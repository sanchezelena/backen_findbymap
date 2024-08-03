from rest_framework import serializers
from supermarket.models.dare import Dare

class DareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dare
        fields = '__all__'