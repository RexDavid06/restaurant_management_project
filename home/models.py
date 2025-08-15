from django.db import models
from products.models import Item

# Create your models here.
class Restuarant(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    phone_number = models.CharField(max_length=17)
    address = models.CharField(max_length=700)

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(amx_digits=1000, decimal_places=2)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item-images')


class RestuarantLocation(models.Model):
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10)
