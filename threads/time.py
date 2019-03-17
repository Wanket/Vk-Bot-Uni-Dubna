from datetime import datetime, timedelta
from time import sleep


def sleep_to_hour(hour):
    now = datetime.today()
    future = datetime(now.year, now.month, now.day, hour) + timedelta(days=1)
    sleep((future - now).seconds)
