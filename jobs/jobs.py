from datetime import datetime
import pytz
import requests
from news.models import Item


def get_single_item(id):
    try:
        news = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty").json()
        if news is not None:
            if not Item.objects.filter(id=id).exists():
                print(f"Saving {id} to the database")
                news['time'] = datetime.utcfromtimestamp(
                    news['time']).replace(tzinfo=pytz.utc)
                Item.objects.create(**news)
            else:
                print(f"{id} already exists in the database")
    except:
        print("Something went Wrong.")


def schedule_latest_item(url):
    data = requests.get(url).json()
    if data is not None:
        if not Item.objects.exists():
            # syncs the db with the first 100 item if the database is empty
            data = data[:100]
        for id in data:
            get_single_item(id)
