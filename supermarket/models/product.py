from django.db import models
from supermarket.models.ubication import Ubication
from supermarket.models.category import Category

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, through='ProductCategory')
    barcode = models.CharField(max_length=100, unique=True)
    units = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offert = models.BooleanField(default=False)
    ubication_id = models.ForeignKey(Ubication, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name