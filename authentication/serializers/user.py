from rest_framework import serializers
from authentication.models.user import User
from administrator.serializers.rol import RolSerializer

class UserSerializer(serializers.ModelSerializer):
    rol = RolSerializer()  

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_admin', 'is_employee', 'rol']
