from django.shortcuts import render
import random
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
# function based view
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,*args , **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        num = None
        condtion_bool_item = True

        if condtion_bool_item:
            num = random.randint(0, 200)

        some_list = [random.randint(0, 100000), random.randint(0, 10000), random.randint(0, 100000)]

        context = {
            "num": num,
            "some_list": some_list
        }

        return context





