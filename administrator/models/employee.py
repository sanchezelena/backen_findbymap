from django.db import models
from administrator.models.rol import Rol

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username= models.Charfield(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    rol = models.ForeignKey(Rol, on_deleete=models.CASCADE)