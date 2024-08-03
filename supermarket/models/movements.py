from django.db import models
from supermarket.models.employee import Employee
from supermarket.models.product import Product

class Movements(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    time = models.TimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units = models.IntegerField()
    category_name = models.CharField(max_length=100)
    quantity = models.IntegerField()