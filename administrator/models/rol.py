from django.db import models

class Rol(models.Model):
    rol_name = models.CharField(max_length=100)
