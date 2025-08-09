from django.urls import path
from .views import *

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('restaurant/', views.RestaurantView.as_view(), name='restaurant'),
]