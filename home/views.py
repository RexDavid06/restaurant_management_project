from django.shortcuts import render
from home.models import Restaurant
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


# Create your views here.
class HomeView(CreateView):
    model = Restaurant.objects.all()
    template_name = 'home/home.html'
    context_object_name = 'restuarant'

class RestaurantView(TemplateView):
    template_name = 'home/restaurant.html'
    

class MenuItemView(CreateView):
    template_name = 'home/menuItem.html'