from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(User):
    name = models.CharField(max_length=255)
    email = models.Email.Field()
    phone_number = models.CharField(max_length=17)

    def __str__(self):
        return self.name
