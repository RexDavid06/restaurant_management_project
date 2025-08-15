from  rest_framework import serializers 
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class meta:
        model = Restaurant
        fields = "__all__"