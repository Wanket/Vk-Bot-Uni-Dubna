from datetime import datetime

from api import send_message
from command.AbstractShedule import AbstractSchedule
from schedule.Lesson import Lesson
from schedule.ScheduleData import ScheduleData
from schedule.default import list_of_lesson_names, default_days_even, default_days_odd


class Schedule(AbstractSchedule):
    def __init__(self):
        super().__init__()
        self.help = "/schedule — работа с расписанием\n"
        self.full_help = "/schedule добавить [день] [номер пары] [аудиторрия] [предмет] [лекция(не обязательно)] — " \
                         "добавить пару в расписание. Например: " \
                         "/schedule добавить ВТ 1 1-118 Экономика лекция\n" \
                         "/schedule изменить [день] [номер пары] [аудиторрия] [предмет] [лекция(не обязательно)] — " \
                         "изменить пару в расписании\n" \
                         "/schedule удалить [день] [пара] — удалить пару\n" \
                         "/schedule показать [день] [пара(не обязательно)] — показать пару или все пары за день\n" \
                         "/schedule сбросить [день] — сбрасывает день в состояние по-умолчанию\n"

    def on_message(self, event, vk):
        spl = event.text.split()

        if len(spl) < 2:
            send_message(event, vk, message=self.full_help)
        elif spl[1] == "сбросить":
            self.reset(event, vk, spl)
        else:
            super().on_message(event, vk)

    def update(self, event, vk, spl):
        if len(spl) < 6:
            send_message(event, vk, message=self.full_help)
            return

        ScheduleData.week.days[ScheduleData.get_day_number(spl[2])].lessons[int(spl[3]) - 1] = Lesson(
            ScheduleData.get_lesson_number(spl[5]), spl[4], len(spl) > 6 and spl[6] == "лекция")

        send_message(event, vk, message="Сделал")

    def delete(self, event, vk, spl):
        if len(spl) < 4:
            send_message(event, vk, message=self.full_help)
            return

        ScheduleData.week.days[ScheduleData.get_day_number(spl[2])].lessons[int(spl[3]) - 1] = Lesson(-1, None, None)

        send_message(event, vk, message="Удалил, а зря!")

    def show(self, event, vk, spl):
        if len(spl) == 3:
            self.show_day(event, vk, spl)
            return

        if len(spl) < 4:
            send_message(event, vk, message=self.full_help)
            return

        lesson = ScheduleData.week.days[ScheduleData.get_day_number(spl[2])].lessons[int(spl[3]) - 1]

        if lesson.lesson_id == -1:
            send_message(event, vk, message="В это время ничего нет.")
            return

        send_message(event, vk, message=f"Я нашел!\nАудитория: {lesson.classroom}, предмет: "
                     f"{list_of_lesson_names[lesson.lesson_id][0]}, {'не ' if not lesson.is_lecture else ''}лекция")

    @staticmethod
    def show_day(event, vk, spl):
        day_name = spl[2]
        message = f"Расписание на {day_name}\n"
        is_found = False
        for lesson in ScheduleData.week.days[ScheduleData.get_day_number(day_name)].lessons:
            if lesson.lesson_id != -1:
                message += f"Аудитория: {lesson.classroom}, предмет: {list_of_lesson_names[lesson.lesson_id][0]}, " \
                    f"{'не ' if not lesson.is_lecture else ''}лекция\n"
                is_found = True

        if is_found:
            send_message(event, vk, message=message)

    def reset(self, event, vk, spl):
        if len(spl) < 3:
            send_message(event, vk, message=self.full_help)
            return

        target_day = ScheduleData.get_day_number(spl[2])
        iso = datetime.today().isocalendar()
        is_even_week = (iso[1] - 1) % 2 == 0 if target_day < iso[2] - 1 else iso[1] % 2 == 0

        ScheduleData.week.days[target_day] = default_days_even[target_day] \
            if is_even_week else default_days_odd[target_day]

        send_message(event, vk, message="Сбросил")
