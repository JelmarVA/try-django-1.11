from django.shortcuts import render
import random
from django.views import View
from django.views.generic import TemplateView
from .models import RestaurantLocation

# Create your views here.
# function based view

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    querysel = RestaurantLocation.objects.all()
    context = {
        "object_list" : querysel
    }
    return render(request, template_name, context)





