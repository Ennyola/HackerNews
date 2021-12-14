from datetime import datetime
import pytz
import requests
from news.models import Item


def get_single_item(id):
    news = requests.get(
        f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty").json()
    if news is not None:
        if Item.objects.filter(id=id).exists():
            print(f"{id} already exists in the database")
        else:
            print(f"Saving {id} to the database")
            news['time'] = datetime.utcfromtimestamp(
                news['time']).replace(tzinfo=pytz.utc)
            Item.objects.create(**news)


def schedule_latest_news():
    try:
        data = requests.get(
            "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty").json()
        if data is not None:
            for id in data:
                get_single_item(id)
    except:
        print("An error occured, please try again later")


def schedule_latest_jobs():
    try:
        data = requests.get(
            "https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty").json()
        if data is not None:
            for id in data:
                get_single_item(id)
    except:
        print("An error occured, please try again later")
