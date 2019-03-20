from datetime import datetime, timedelta
from time import sleep


def sleep_to_hour(hour):
    now = datetime.today()
    if now.hour >= hour:
        future = datetime(now.year, now.month, now.day, hour) + timedelta(days=1)
    else:
        future = datetime(now.year, now.month, now.day, hour)

    sleep((future - now).seconds + 10)
