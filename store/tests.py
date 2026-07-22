from django.test import TestCase
from store.models import Store, Item, Address

# Create your tests here.
class StoreTestCase(TestCase):
    def setUp(self):
        test_store = Store.objects.create(name="Costco")
        
        if test_store.name != 'Costco':
            raise ValueError("StoreTestCase error in Create!")
        
        