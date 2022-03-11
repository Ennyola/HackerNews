from django.test import TestCase
from ..models import Item

class TestModels(TestCase):        
    def test_title_returned(self):
        item = Item.objects.create(id=34092,by="Enny",type="job",title="A new Dawn")
        self.assertEqual(str(item),item.title)