from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')