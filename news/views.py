import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import Item
from .helpers import get_searched_item
# Create your views here.


def list_news(request):
    # fetch all news from database
    news = Item.objects.all()
    context = {'title': 'Latest News'}
    get_searched_item(request, news, context)
    return render(request, "news/news_list.html", context)

def type_job(request):
    # filters news with type job
    news = Item.objects.filter(type="job")
    context = {'title': 'Job'}
    get_searched_item(request, news, context)
    return render(request, "news/news_list.html", context)


def ask_hn(request):
    # filters news for ask hn
    news = Item.objects.filter(text__isnull=False, url__isnull=True).exclude(
        title__startswith="show hN:")
    context = {'title': 'Ask HN'}
    get_searched_item(request, news, context)
    return render(request, "news/news_list.html", context)


def show_hn(request):
    news = Item.objects.filter(
        text__isnull=False, title__startswith="show hN:")
    context = {'title': 'Show HN'}
    get_searched_item(request, news, context)
    return render(request, "news/news_list.html", context)


def news_details(request, id):
    '''checks for comments for a single news item
    and then parses the comment into a string 
    since HTML elements are a part of the comment 
    '''
    news = Item.objects.get(id=id)
    comments = []
    if news.kids:
        for id in news.kids:
            try:
                comment = requests.get(
                    f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty").json()
                soup = BeautifulSoup(comment['text'], 'html.parser')
                comment['text'] = soup.get_text()
                comments.append(comment)
            except:
                print("something went wrong")

    context = {
        "news": news,
        "comments": comments
    }
    return render(request, 'news/news_detail.html', context)
