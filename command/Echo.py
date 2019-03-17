from Message import Message
from api import send_message
from command.Command import Command


class Echo(Command):
    def __init__(self):
        super().__init__()
        self.help = "/echo — повторение введенного сообщения\n"
        self.full_help = "/echo [сообщение для повтора] — повторить сообщение полностью\n"

    def on_message(self, event, vk):
        message = Message(event)

        parse_text = message.text.replace("/echo ", "", 1)

        if message.is_empty("/echo"):
            send_message(event, vk, message="И как мне предлагаешь повторить пустое сообщение?")
        elif parse_text == "":
            send_message(event, vk, attachment=message.attachments, forward_messages=message.forward_messages,
                         reply_to=message.reply_to)
        else:
            send_message(event, vk, message=f'{parse_text}', attachment=message.attachments,
                         forward_messages=message.forward_messages, reply_to=message.reply_to)
