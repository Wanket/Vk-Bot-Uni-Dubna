from datetime import datetime
from threading import Thread
from time import sleep

from api import send_message
from schedule.ScheduleData import ScheduleData
from schedule.default import list_of_lesson_names
from threads.NextDayHomework import PseudoEvent
from threads.time import sleep_to_hour


class NextLesson(Thread):
    time_schedule = [(8, 40), (10, 20), (12, 30), (14, 10), (15, 50), (17, 30)]

    def __init__(self, chat_id, vk):
        super().__init__()
        self.event = PseudoEvent(chat_id)
        self.vk = vk

    def run(self):
        while True:
            sleep_to_hour(7)
            now = datetime.today()

            if now.isocalendar()[2] == 7:
                continue

            for i, value in enumerate(self.time_schedule):
                if now.hour < value[0] or now.hour == value[0] and now.minute < value[1]:
                    sleep_to_hour(value[0])
                    sleep(value[1] * 60)

                    now = datetime.today()
                    lesson = ScheduleData.week.days[now.isocalendar()[2] - 1].lessons[i]
                    if lesson.lesson_id != -1:
                        lesson_name = list_of_lesson_names[lesson.lesson_id][0]
                        ScheduleData.homework[lesson.lesson_id] = None
                        send_message(self.event, self.vk, message=f"В {self.time_schedule[i][0]}:"
                                     f"{self.time_schedule[i][1] + 20} "
                                     f"будет {'лекция' if lesson.is_lecture else 'семинар'} по {lesson_name} "
                                     f"в кабинете {lesson.classroom}")
