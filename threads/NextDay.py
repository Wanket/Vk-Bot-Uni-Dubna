from datetime import datetime
from threading import Thread

from schedule.ScheduleData import ScheduleData
from threads.time import sleep_to_hour


class NextDay(Thread):
    def run(self):
        while True:
            sleep_to_hour(3)
            if datetime.today().isocalendar()[2] == 7:
                continue

            ScheduleData.week.reload_next_day()
