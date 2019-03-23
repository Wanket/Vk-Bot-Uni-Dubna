from datetime import datetime
from threading import Thread

from command import Homework
from schedule.ScheduleData import ScheduleData
from schedule.default import list_of_week_days_names
from threads.time import sleep_to_hour


class PseudoEvent:
    def __init__(self, chat_id):
        self.chat_id = chat_id


class NextDayHomework(Thread):
    def __init__(self, chat_id, vk):
        super().__init__()
        self.event = PseudoEvent(chat_id)
        self.vk = vk

    def run(self):
        while True:
            sleep_to_hour(20)
            week_day = datetime.today().isocalendar()[2]
            if week_day == 6:
                continue

            if week_day == 7:
                week_day = 0

            for lesson in ScheduleData.week.days[week_day].lessons:
                if lesson.lesson_id != -1:
                    Homework.show_day(self.event, self.vk, list_of_week_days_names[week_day][0])
                    break
