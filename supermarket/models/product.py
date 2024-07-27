from django.db import models
from supermarket.models.ubication import Ubication
from supermarket.models.category import Category

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, through='ProductCategory')
    barcode = models.CharField(max_length=100, unique=True)
    units = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offert = models.BooleanField(default=False)
    ubication = models.ForeignKey(Ubication, on_delete=models.CASCADE)
