from django.shortcuts import render
from home.models import Restaurant
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User


# Create your views here.
class HomeView(CreateView):
    model = Restaurant.objects.all()
    template_name = 'home/home.html'
    context_object_name = 'restuarant'

    def get_queryset():
        user = User.objects.filter(is_staff=True)
        try:
            if user is not None:
                return f"{user.username} is a staff"
        except Exception as e:
            print(f"Not a staff {e}")
            return None


class RestaurantView(TemplateView):
    template_name = 'home/restaurant.html'
    

class MenuItemView(CreateView):
    template_name = 'home/menuItem.html'