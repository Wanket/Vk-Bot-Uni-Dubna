from threading import Thread
from time import sleep

from schedule.ScheduleData import ScheduleData


class SyncSchedule(Thread):
    def run(self):
        while True:
            sleep(60 * 10)

            with open("save_schedule/schedule", "wb") as f:
                f.write(ScheduleData.dump())
