from django.db.models import Q
from django.shortcuts import render, get_object_or_404
import random
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView
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

class RestaurantDetailView(DetailView):
    queryset =  RestaurantLocation.objects.all()

    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get("rest_id")
        obj = get_object_or_404(RestaurantLocation, id=rest_id)
        return obj

