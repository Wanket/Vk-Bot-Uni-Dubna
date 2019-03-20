import pickle
from os.path import isfile

from schedule.Week import Week
from schedule.default import list_of_week_days_names, list_of_lesson_names


class ScheduleData(object):
    homework = None
    week = None

    @staticmethod
    def get_day_number(name):
        return next(i for i, x in enumerate(list_of_week_days_names) if name.lower() in x)

    @staticmethod
    def get_lesson_number(name):
        return next(i for i, x in enumerate(list_of_lesson_names) if name.lower() in x)

    @staticmethod
    def dump():
        return pickle.dumps((ScheduleData.week, ScheduleData.homework))

    @staticmethod
    def load(schedule_data_bytes):
        tup = pickle.loads(schedule_data_bytes)
        ScheduleData.week = tup[0]
        ScheduleData.homework = tup[1]

    @staticmethod
    def init():
        if isfile("save_schedule/schedule"):
            with open("save_schedule/schedule", "rb") as f:
                ScheduleData.load(f.read())
        else:
            ScheduleData.week = Week.generate_current_week()
            ScheduleData.homework = [None, None, None, None, None, None, None, None, None]


ScheduleData.init()
