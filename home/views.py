from django.shortcuts import render
from home.models import Restaurant
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    model = Restaurant.objects.all()
    template_name = 'home/home.html'
    context_object_name = 'restuarant'

