from django.shortcuts import render
from .models import Restaurant, RestaurantLocation
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RestaurantSerializer


# Create your views here.
class HomeView(CreateView):
    model = Restaurant.objects.all()
    template_name = 'home/home.html'
    context_object_name = 'restuarant'

    def get_queryset(self):
        user = User.objects.get(is_staff=True)
        try:
            if user is not None:
                return f"{user.username} is a staff"
        except User.DoesNotExist:
            raise ValueError("User isnt a staff")
            


class RestaurantView(CreateView):
    model = RestaurantLocation.objects.all()
    template_name = 'home/restaurant.html'
    

class MenuItemView(CreateView):
    template_name = 'home/menuItem.html'


@api_view(["GET"])
def restaurant_info(request, pk):
    try:
        restuarant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response({"error": 'restuarant not found'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = RestaurantSerializer(restaurant)
    return Response(serializer.data, status=status.HTTP_200_OK)