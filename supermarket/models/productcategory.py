from django.db import models
from supermarket.models.category import Category
from supermarket.models.product import Product

class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)