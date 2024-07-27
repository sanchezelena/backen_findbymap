from rest_framework import viewsets
from administrator.serializers.employee import EmployeeSerializer
from administrator.models.employee import Employee

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer