from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin

class Creacion(LoginRequiredMixin, models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField()
    product_picture = models.ImageField(upload_to='product_image', null=True, blank=True)
    

    def __str__(self):
        return self.name





