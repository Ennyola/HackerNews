import requests


def check_for_news(id):
    news = requests.get(
        f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty").json()
    return news


def check_for_max_item():
    item = requests.get(
        f"https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty").json()
    return item
