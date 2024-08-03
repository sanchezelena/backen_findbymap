from django.db import models
from supermarket.models.ubication import Ubication

class Dare(models.Model):
    message = models.TextField()
    ubication = models.ForeignKey(Ubication, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    finish = models.DateTimeField()
    visible = models.BooleanField(default=True)