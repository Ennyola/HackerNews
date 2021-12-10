from datetime import datetime
import pytz
import requests
from news.models import News


def get_single_news(id):
    news = requests.get(
        f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty").json()
    if news is not None:
        if News.objects.filter(id=id).exists():
            print(f"{id} already exists in the database")
        else:
            print(f"Saving {id} to the database")
            news['time'] = datetime.utcfromtimestamp(
                news['time']).replace(tzinfo=pytz.utc)
            News.objects.create(**news)


def schedule_api():
    try:
        data = requests.get(
            "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty").json()
        if data is not None:
            for id in data:
                get_single_news(id)
    except:
        pass
