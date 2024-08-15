from django.db import models
from authentication.models.user import User
from supermarket.models.product import Product, Ubication

class Movements(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    time = models.TimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    ubication = models.ForeignKey(Ubication, on_delete=models.CASCADE)

    def __str__(self):
        return f"Movimiento del producto {self.product.product_name} por {self.employee.username} a pasillo {self.ubication.shelf} y estante {self.ubication.aisle}"