from django.db import models

class Ubication(models.Model):
    aisle = models.CharField(max_length=100)
    shelf = models.CharField(max_length=100)


    def __str__(self):
        return f"Aisle {self.aisle}, Shelf {self.shelf}"