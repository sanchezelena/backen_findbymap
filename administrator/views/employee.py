from rest_framework import viewsets
from administrator.serializers.employee import EmployeeSerializer
from administrator.models.employee import Employee
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from http import HTTPStatus
from rest_framework.decorators import action


class EmployeeAdminViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]

    @action(detail=False, methods=['get'], url_path='all')
    def list_employees(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=HTTPStatus.OK)
    
    @action(detail=False, methods=['get'], url_path='employeee/[id]')
    def get_employee(self, request, pk=None):
            try:
                employee = Employee.objects.get(pk=pk)
                serializer = EmployeeSerializer(employee)
                return Response(serializer.data, status=HTTPStatus.OK)
            except Employee.DoesNotExist:
                return Response(status=HTTPStatus.NOT_FOUND)
            
    @action(detail=False, methods=['post'], url_path='create')
    def create_employee(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.CREATED)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
    
    @action(detail=False, methods=['put'], url_path='update')
    def update_employee(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response(status=HTTPStatus.NOT_FOUND)
        
    @action(detail=False, methods=['delete'], url_path='delete')
    def delete_employee(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()
            return Response(status=HTTPStatus.NO_CONTENT)
        except Employee.DoesNotExist:
            return Response(status=HTTPStatus.NOT_FOUND)