from os.path import isfile

from Message import Message
from api import send_message
from command.Command import Command


class Remind(Command):
    def __init__(self):
        super().__init__()
        self.help = "/remind [ключевое слово]"
        self.full_help = self.help + "Ключевое слово может быть только одно. " \
                                     "Для использования нескольких ключевых слов, можно, например, добавлять \"_\": " \
                                     "одно_слово_и_другое_слово\nОстальная часть команды игнорируется"

    def on_message(self, event, vk):
        message = Message(event)

        if message.is_empty("/remind"):
            send_message(event, vk,
                         message="И как мне предлагаешь вспомнить по пустому ключу?")
            return

        spl = message.text.split()[1]

        if spl[1].find("/"):
            send_message(event, vk, message="Иньекцию захотел сделать? А вот хрен!")
            return

        if not isfile(f"save/{spl}"):
            send_message(event, vk,
                         message=f"Сообщение по ключу {spl} не найдено")

        with open(f"save/{spl}", "rb") as f:
            message = Message.load(f.read())

            send_message(event, vk,
                         message=message.text.replace("/remember", "", 1).replace(spl, "", 1),
                         attachment=message.attachments,
                         forward_messages=message.forward_messages,
                         reply_to=message.reply_to)
