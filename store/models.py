"""
| This page serves as the relational schema outlay for the project. It contains
| class definitions for the three classes - store, address and item. Item and
| store are weak entities attached to the 'Store' strong entity.
| The item's weak entity linking approach taken from here: https://stackoverflow.com/questions/22577060/weak-entities-in-django
| The address's weak entity definition taken from here: https://claude.ai/chat/83b7f8a6-8bf6-4945-b60a-84d23ff41a24

Let's see which one works better!

"""

from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Address(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="addresses")
    line = models.CharField(max_length=255)

    class Meta:
        unique_together = ('store', 'line')

class Item(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='items')
    name  = models.CharField(max_length=100)
    unitCost = models.FloatField()
    weightKg = models.FloatField()
    
    class Meta:
        unique_together = ('store', 'name')

