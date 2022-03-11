from cgitb import lookup
from turtle import update
from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED
from urllib3 import Retry
from news.models import Item
from .serializers import NewsSerializer
from .helpers import check_for_news, check_for_max_id

# Create your views here.

class News(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = NewsSerializer
#   Filters the news based on title, type and author(by)
    filterset_fields = {
        'by': ["exact", 'iexact'],
        'title': ['exact', 'iexact', 'icontains'],
        'type': ['exact', 'iexact'],
    }

    def create(self, request):
        '''
        uses the max item endpoint
        in the api to ensure no data
        can be created that exists in hackernews already
        '''
        try:
            max_id = check_for_max_id()
            if int(max_id) >= int(request.data['id']):
                return Response("Item Already exists in HackerNews API", status=HTTP_400_BAD_REQUEST)
            else:
                return super().create(request)
        except:
            return Response("Unexpected Error. Please try again", status=HTTP_500_INTERNAL_SERVER_ERROR)


class singleNews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'

    def update(self, request, id):
        '''
        checks if the item exits in hackernews before updating occurs
        If the item exits, it cannot be updated
        '''
        try:
            news = check_for_news(id)
            if news:
                return Response("Cannot update news from hackernews", status=HTTP_400_BAD_REQUEST)
        except:
            return Response("Unexpected Error", status=HTTP_500_INTERNAL_SERVER_ERROR)
        return super().update(request, id)

    def destroy(self, request, id):
        '''
        checks if the item exits in hackernews before deleting occurs
        If the item exits, it cannot be deleted
        '''
        try:
            news = check_for_news(id)
            if news:
                return Response("Cannot Delete news from hackernews", status=HTTP_400_BAD_REQUEST)
        except:
            return Response("Unexpected Error", status=HTTP_500_INTERNAL_SERVER_ERROR)
        return super().destroy(request, id)
