from django.db import models

class Ubication(models.Model):
    aisle = models.CharField(max_length=100)
    shelf = models.CharField(max_length=100)
