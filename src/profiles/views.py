from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from restaurants.models import RestaurantLocation
from menus.models import Item

User = get_user_model()

class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'

    def get_object(self):
        username = self.kwargs["username"]

        if username is None:
            raise Http404

        return get_object_or_404(User, username=username, is_active= True)


    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)

        user = context['user']
        query = self.request.GET['q']
        items_exist = Item.objects.filter(user=user).exists()
        qs = RestaurantLocation.objects.filter(owner=user).search(query)

        if qs.exists() and items_exist:
            context['locations'] = qs

        return context
