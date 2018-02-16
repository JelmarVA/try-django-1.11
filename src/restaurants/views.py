from django.db.models import Q
from django.shortcuts import render
import random
from django.views import View
from django.views.generic import ListView, TemplateView
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

class RestaurantListView(ListView):
    queryset =  RestaurantLocation.objects.all()
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):

        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__contains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

