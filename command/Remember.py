from Message import Message
from api import send_message
from command.Command import Command


class Remember(Command):
    def __init__(self):
        super().__init__()
        self.help = "/remember — запомнить сообщение\n"
        self.full_help = "/remember [ключевое слово] [сообщение для запоминания] — запомнить сообщение по ключевому " \
                         "слову\n" \
                         "Ключевое слово может быть только одно. " \
                         "Для использования нескольких ключевых слов, можно, например, добавлять \"_\": " \
                         "одно_слово_и_другое_слово"

    def on_message(self, event, vk):
        message = Message(event)

        spl = message.text.split()
        if len(spl) < 3 and message.is_empty_except_text():
            send_message(event, vk, message="И как мне предлагаешь запомнить пустое сообщение?")
            return

        dump = message.dump()

        try:
            if spl[1].find("/") != -1:
                send_message(event, vk, message="Иньекцию захотел сделать? А вот хрен!")
                return

            with open(f"save/{spl[1]}", "wb") as f:
                f.write(dump)

            send_message(event, vk, message="Я запомнил!")
        except IOError:
            send_message(event, vk, message="Невалидный ключ")
