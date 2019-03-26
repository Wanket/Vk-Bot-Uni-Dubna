from api import send_message
from command.AbstractShedule import AbstractSchedule
from schedule.ScheduleData import ScheduleData
from schedule.default import list_of_lesson_names


class Homework(AbstractSchedule):
    def __init__(self):
        super().__init__()
        self.help = "/homework — работа с дз\n"
        self.full_help = "/homework добавить [предмет] [дз/пересланное сообщение] — добавить дз для предмета\n" \
                         "/homework изменить [предмет] [дз/пересланное сообщение] — изменить дз для предмета\n" \
                         "/homework удалить [предмет] — удалить дз для предмета\n" \
                         "/homework показать [предмет/день] — показать дз для предмета/за день. Например: " \
                         "/homework показать Экономика или /homework показать ВТ\n"

    def update(self, event, vk, spl):
        if len(spl) < 3:
            send_message(event, vk, message=self.full_help)
            return

        if len(spl) > 3:
            ScheduleData.homework[ScheduleData.get_lesson_number(spl[2])] = event.text.replace("/homework ", "", 1)\
                .replace(spl[1], "", 1).replace(spl[2], "", 1)
            send_message(event, vk, message="Добавил")
            return

        if len(spl) == 3:
            if "reply_message" in event.message_data and "text" in event.message_data["reply_message"]\
                    and event.message_data["reply_message"]["text"] != "":
                ScheduleData.homework[ScheduleData.get_lesson_number(spl[2])] \
                    = event.message_data["reply_message"]["text"]
                send_message(event, vk, message="Добавил")
            elif "fwd_messages" in event.message_data and len(event.message_data["fwd_messages"]) != 0 \
                    and "text" in event.message_data["fwd_messages"][0] \
                    and event.message_data["fwd_messages"][0]["text"] != "":
                ScheduleData.homework[ScheduleData.get_lesson_number(spl[2])] \
                    = event.message_data["fwd_messages"][0]["text"]
                send_message(event, vk, message="Добавил")
            else:
                send_message(event, vk, message=self.full_help)

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
            send_message(event, vk, message=f"{list_of_lesson_names[ScheduleData.get_lesson_number(spl[2])][0]}:"
                                            f" {homework}" if homework is not None else "Ничего нет, радуйтесь!")
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
            if homework is not None and not lesson.is_lecture:
                is_found = True
                message += f"{list_of_lesson_names[lesson.lesson_id][0]}: {homework}\n"
        send_message(event, vk, message=message if is_found else f"Ничего на {day_name} нет, радуйтесь!")
