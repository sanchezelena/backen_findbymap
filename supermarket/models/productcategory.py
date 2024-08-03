from django.db import models
from supermarket.models.category import Category
from supermarket.models.product import Product

class ProductCategory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE,  primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.product_name} - {self.category.category_name}"