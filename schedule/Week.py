from datetime import datetime

from schedule.default import default_days_even, default_days_odd


class Week:
    def __init__(self, days, next_load_date):
        self.next_load_date = next_load_date
        self.days = days

    def reload_next_day(self):
        is_even_week = (self.next_load_date[1] - 1) % 2 == 0
        self.days[self.next_load_date[2] - 1] = default_days_even[self.next_load_date[2] - 1] \
            if is_even_week else default_days_odd[self.next_load_date[2] - 1]

        self.next_load_date[2] += 1
        if self.next_load_date[2] == 7:
            self.next_load_date[2] = 1
            self.next_load_date[1] += 1

    @staticmethod
    def generate_current_week():
        today = list(datetime.today().isocalendar())
        is_even_week = (today[1] - 1) % 2 == 0

        days = [None, None, None, None, None, None]
        for i in range(6):
            if today[2] == 7:
                today[2] = 1
                today[1] += 1

            days[today[2] - 1] = default_days_even[today[2] - 1] if is_even_week else default_days_odd[today[2] - 1]

            today[2] += 1
            is_even_week = (today[1] - 1) % 2 == 0

        return Week(days, today)
