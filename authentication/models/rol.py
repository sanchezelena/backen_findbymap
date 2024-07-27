from django.db import models

class Rol(models.Model):
    rol_name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.rol_name