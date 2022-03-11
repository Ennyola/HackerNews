from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_latest_item


def start():
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(lambda:schedule_latest_item("https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"), 'interval', minutes=5)
    scheduler.add_job(lambda:schedule_latest_item("https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty"), 'interval', minutes=5)
    scheduler.add_job(lambda:schedule_latest_item("https://hacker-news.firebaseio.com/v0/askstories.json?print=pretty"), 'interval', minutes=5)
    scheduler.add_job(lambda:schedule_latest_item("https://hacker-news.firebaseio.com/v0/showstories.json?print=pretty"), 'interval', minutes=5)
