from schedule.Day import Day
from schedule.Lesson import Lesson

default_days_even = \
    [
        Day([
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(0, "1-120", True),
            Lesson(1, "1-431", False),
            Lesson(5, "4-418", False),
            Lesson(-1, None, None)
        ]),
        Day([
            Lesson(2, "1-118", True),
            Lesson(3, "1-213", False),
            Lesson(4, "с/к Олимп", False),
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None)
        ]),
        Day([
            Lesson(-1, None, None),
            Lesson(2, "2-310", False),
            Lesson(4, "c/к Олмип", False),
            Lesson(5, "2-304а", False),
            Lesson(-1, None, None),
            Lesson(-1, None, None)
        ]),
        Day([
            Lesson(6, "1-118", True),
            Lesson(2, "2-310", False),
            Lesson(4, "c/к Олмип", False),
            Lesson(1, "1-122", True),
            Lesson(-1, None, None),
            Lesson(-1, None, None)
        ]),
        Day([
            Lesson(6, "1-213", False),
            Lesson(7, "1-318", False),
            Lesson(8, "3-100", False),
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None)
        ]),
        Day([
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None)
        ]),
    ]

default_days_odd = \
    [
        Day([
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(0, "1-120", True),
            Lesson(1, "1-431", False),
            Lesson(5, "4-418", False),
            Lesson(-1, None, None)
        ]),
        Day([
            Lesson(2, "1-118", True),
            Lesson(3, "1-213", False),
            Lesson(4, "с/к Олимп", False),
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None)
        ]),
        Day([
            Lesson(2, "1-118", True),
            Lesson(2, "2-310", False),
            Lesson(4, "c/к Олмип", False),
            Lesson(5, "2-304а", False),
            Lesson(-1, None, None),
            Lesson(-1, None, None)
        ]),
        Day([
            Lesson(6, "1-118", True),
            Lesson(0, "5-314", False),
            Lesson(4, "c/к Олмип", False),
            Lesson(1, "1-122", True),
            Lesson(-1, None, None),
            Lesson(-1, None, None)
        ]),
        Day([
            Lesson(6, "1-213", False),
            Lesson(7, "1-318", False),
            Lesson(8, "3-100", False),
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None)
        ]),
        Day([
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None)
        ]),
    ]

list_of_lesson_names = \
    [
        ["Экономика", "экономика"],
        ["ПЯВУ", "пяву"],
        ["Мат.Ан.", "матан", "мат"],
        ["КП", "кп"],
        ["Физ-ра", "ЭДФКиС", "физра", "физкультура"],
        ["Ин.яз.", "иняз", "англ", "английский"],
        ["ИСиТ", "ист", "исит"],
        ["ОИТ", "оит"],
        ["ИГ", "иг"],
    ]

list_of_week_days_names = \
    [
        ["ПН", "пн", "понедельник"],
        ["ВТ", "вт", "вторник"],
        ["СР", "ср", "среда"],
        ["ЧТ", "чт", "четверг"],
        ["ПТ", "пт", "пятница"],
        ["СБ", "сб", "суббота"]
    ]
