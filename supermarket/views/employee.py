from rest_framework import viewsets
from supermarket.models.employee import Employee
from supermarket.serializers.employee import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer