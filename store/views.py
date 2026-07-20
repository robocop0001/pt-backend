"""
| Viewsets and routers are simple tools to speed up the implementation of the
| API, assuming standard behaviour and URLs. Viewsets are preferred to views
| because I won't have to 'create separate views' for getting a list of
| objects and details of an object. 
| Routers are used with viewsets together because they create a standardised
| structure of URLS (consistent by the creators of Django REST framework).
| Sourced here: https://stackoverflow.com/questions/32589087/difference-between-views-and-viewsets

Let's see how this works!
"""

from django.shortcuts import render

from django.shortcuts import viewsets
from rest_framework.permissions import AllowAny
from store.models import Store, Item, Address
from store.serializers import StoreSerializer, ItemSerializer, AddressSerializer

# Create your views here.

# think of viewsets as a restaurant kitchen and queryset as the ingredients in
# the pantry. this solution has a static queryset, meaning that every
# ingredient in the main pantry is available for every order. dynamic querysets
# exist for multi-layered permission access models, but I won't be worrying
# about that for now.

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [AllowAny] # any user can make CRUD changes, auth later

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [AllowAny]

