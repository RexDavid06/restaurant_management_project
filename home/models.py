from django.db import models

# Create your models here.
class Restuarant(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    phone_number = models.CharField(max_length=17)

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.name

    