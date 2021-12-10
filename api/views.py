from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from news.models import News
from .serializers import NewsSerializer
from .helpers import check_for_news, check_for_max_item

# Create your views here.


class GetNews(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        """
        Filters the news based on title, type and author(by)
        """
        queryset = News.objects.all()
        title = self.request.query_params.get('title', None)
        type = self.request.query_params.get('type', None)
        by = self.request.query_params.get('by', None)

        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if type is not None:
            queryset = queryset.filter(type__icontains=type)
        if by is not None:
            queryset = queryset.filter(by__icontains=by)
        return queryset

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, id=None):
        '''
        uses the max item endpoint 
        in the api to ensure no data 
        can be created that exists in hackernews already
        '''
        try:
            item = check_for_max_item()
            if int(item) >= int(request.data['id']):
                return Response("News Already exists in HackerNews", status=HTTP_400_BAD_REQUEST)
            else:
                return self.create(request)
        except:
            return Response("Unexpected Error", status=HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id=None):
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
        return self.update(request, id)

    def delete(self, request, id=None):
        '''
        checks if the item exits in hackernews before deleting occurs
        If the item exits, it cannot be deleted
        '''
        try:
            news = check_for_news(id)
            if news:
                return Response("Cannot Delete news gotten from hackernews", status=HTTP_400_BAD_REQUEST)
            else:
                return self.destroy(request, id)
        except:
            return Response("Unexpected Error", status=HTTP_500_INTERNAL_SERVER_ERROR)
