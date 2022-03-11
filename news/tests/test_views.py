from django.test import TestCase,Client
from django.urls import reverse
from ..models import Item
class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        Item.objects.create(id=34092,by="Enny",type="job",title="A new Dawn")
        
        
    def test_list_news_url(self):
        response= self.client.get(reverse("index"))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'news/news_list.html')
        
    def test_job_view(self):
        response= self.client.get(reverse("job"))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'news/news_list.html')
    
    def test_ask_hn_view(self):
        response= self.client.get(reverse("ask"))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'news/news_list.html')
    
    def test_show_hn_view(self):
        response= self.client.get(reverse("show"))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'news/news_list.html')
        
    def test_news_details_view(self):
        response= self.client.get(reverse("details",args=['34092']))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'news/news_detail.html')
        
        