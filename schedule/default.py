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
            Lesson(-1, None, None),
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
            Lesson(6, "1-213", None),
            Lesson(7, "1-318", None),
            Lesson(8, "1-427", None),
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
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None),
            Lesson(-1, None, None)
        ]),
        Day([
            Lesson(2, "1-118", False),
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
            Lesson(6, "1-213", None),
            Lesson(7, "1-318", None),
            Lesson(8, "1-427", None),
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
        ["Экономика"],
        ["ПЯВУ"],
        ["Мат.Ан."],
        ["КП"],
        ["Физ-ра", "ЭД ФКиС"],
        ["Ин.яз."],
        ["ИСиТ"],
        ["ОИТ"],
        ["ИГ"],
    ]

list_of_week_days_names = \
    [
        ["ПН"],
        ["ВТ"],
        ["СР"],
        ["ЧТ"],
        ["ПТ"],
        ["СБ"]
    ]
