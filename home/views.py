from django.shortcuts import render
from home.models import Restaurant

# Create your views here.
class HomeView(TemplateView):
    model = Restaurant
    template_name = 'home/home.html'
    context_object_name = 'restuarant'

