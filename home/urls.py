from django.urls import path
from .views import *

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('restaurant/', views.RestaurantView.as_view(), name='restaurant'),
    path('menuItem/', views.MenuItemView.as_view(), name='menuItem'),
    path("restuarant_info/<int:pk>/", views.restuarant_info, name='restuarant_info')
]