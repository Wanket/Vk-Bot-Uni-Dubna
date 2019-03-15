from datetime import datetime

from api import send_message
from command.Command import Command
from schedule.ScheduleData import ScheduleData
from schedule.default import default_days_even, default_days_odd


class Day(Command):
    def __init__(self):
        super().__init__()
        # TODO: добавить справку
        self.help = "Тут будет справка"
        self.full_help = "Тут будет справка"

    def on_message(self, event, vk):
        spl = event.text.split()
        if len(spl) < 2:
            send_message(event, vk, message=self.full_help)
        elif spl[1] == "сбросить":
            self.reset(event, vk, spl)
        else:
            send_message(event, vk, message=self.full_help)

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
