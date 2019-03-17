from Message import Message
from api import send_message
from command.Command import Command, commands


class Help(Command):
    def __init__(self):
        super().__init__()
        self.help = "/help — показать справку\n"
        self.full_help = "/help — показать справку обо всех командах\n" \
                         "/help [команда] — показать полную справку по команде\n"

    def on_message(self, event, vk):
        message = Message(event)

        if not message.is_empty("/help"):
            key = message.text.replace("/help ", "/", 1)
            if key in commands:
                command = commands[key]
                send_message(event, vk, message=command.full_help)
                return

        message = "Список возможных команд:\n"
        for command in commands.values():
            message += command.help

        send_message(event, vk, message=message)
