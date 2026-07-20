"""
| Serializers weren't automatically generated with the boilerplate I activated
| for this application. I made this. I also used nested serializers to handle
| foreign keys as per this Stack Overflow thread: https://stackoverflow.com/questions/75386610/how-to-serialize-django-model-with-2-or-more-foreign-keys
| Serializers convert incoming data from another language into Python, and also
| output data from database into a consumable format like JSON.
"""

from rest_framework import serializers
from .models import Store, Address, Item

class StoreSerializer(serializers.Serializer):
    class Meta:
        model = Store
        fields = '__all__'
        read_only_fields = '__all__'

class AddressSerializer(serializers.Serializer):
    store = StoreSerializer()

    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ['store']

class ItemSerializer(serializers.Serializer):
    store = StoreSerializer()

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['name']