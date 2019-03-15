from api import send_message
from command.AbstractShedule import AbstractSchedule
from schedule.ScheduleData import ScheduleData
from schedule.default import list_of_lesson_names


class Homework(AbstractSchedule):
    def __init__(self):
        super().__init__()
        # TODO: добавить справку
        self.help = "Тут будет справка"
        self.full_help = "Тут будет справка"

    def update(self, event, vk, spl):
        if len(spl) < 4:
            send_message(event, vk, message=self.full_help)
            return

        ScheduleData.homework[ScheduleData.get_lesson_number(spl[2])] = event.text.replace("/homework ", "", 1).replace(
            spl[1], "", 1).replace(spl[2], "", 1)
        send_message(event, vk, message="Сделал")

    def delete(self, event, vk, spl):
        if len(spl) < 3:
            send_message(event, vk, message=self.full_help)
            return

        ScheduleData.homework[ScheduleData.get_lesson_number(spl[2])] = None
        send_message(event, vk, message="Не хочется делать, да?")

    def show(self, event, vk, spl):
        if len(spl) < 3:
            send_message(event, vk, message=self.full_help)
            return

        try:
            homework = ScheduleData.homework[ScheduleData.get_lesson_number(spl[2])]
            send_message(event, vk, message=homework if homework is not None else "Ничего нет, радуйтесь!")
        except StopIteration:
            self.show_day(event, vk, spl[2])

    @staticmethod
    def show_day(event, vk, day_name):
        message = f"Дз на {day_name}\n"
        is_found = False
        for lesson in ScheduleData.week.days[ScheduleData.get_day_number(day_name)].lessons:
            if lesson.lesson_id == -1:
                continue

            homework = ScheduleData.homework[lesson.lesson_id]
            if homework is not None:
                is_found = True
                message += f"{list_of_lesson_names[lesson.lesson_id][0]}: {homework}\n"
        send_message(event, vk, message=message if is_found else f"Ничего на {day_name} нет, радуйтесь!")
