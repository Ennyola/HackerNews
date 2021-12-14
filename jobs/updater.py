from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_latest_news, schedule_latest_jobs


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_latest_news, 'interval', minutes=5)
    scheduler.add_job(schedule_latest_jobs, 'interval', minutes=5)
    scheduler.start()
