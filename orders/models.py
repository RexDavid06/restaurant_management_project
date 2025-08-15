from django.db import models

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_item = models.ForeignKey(Item, on_delete.models.CASCADE)
    total_amount = models.CharField(max_length=100)
    order_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        
