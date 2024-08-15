from django.db import models

class Rol(models.Model):
    rol_name = models.CharField(max_length=50)

    def __str__(self):
        return self.rol_name
