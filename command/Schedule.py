from api import send_message
from command.AbstractShedule import AbstractSchedule
from schedule.Lesson import Lesson
from schedule.ScheduleData import ScheduleData
from schedule.default import list_of_lesson_names


class Schedule(AbstractSchedule):
    def __init__(self):
        super().__init__()
        # TODO: добавить справку
        self.help = "Тут будет справка"
        self.full_help = "Тут будет справка"

    def update(self, event, vk, spl):
        if len(spl) < 6:
            send_message(event, vk, message=self.full_help)
            return

        ScheduleData.week.days[ScheduleData.get_day_number(spl[2])].lessons[int(spl[3]) - 1] = Lesson(
            ScheduleData.get_lesson_number(spl[5]), spl[4], True if len(spl) > 6 and spl[6] == "лекция" else False)

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
