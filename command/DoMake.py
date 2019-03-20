import random
from api import send_message
from command.Command import Command


class Make(Command):
    def __init__(self):
        super().__init__()
        self.help = "/сделай [сообщение] - just for lulz"
        self.full_help = "/сделай [сообщение] - just for lulz"

    def on_message(self, event, vk):
        spl = event.text.split()

        if len(spl) < 2:
            send_message(event, vk, message="И как я тебе должен сделать - ничего??")
            return

        send_message(event, vk, message=f"Я сделаю {spl[1]}, за {random.randint(100, 2000)} ))0)")
