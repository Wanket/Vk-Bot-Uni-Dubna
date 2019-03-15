from api import send_message


def on_message(event, vk):
    key = event.text.split()[0]

    if "payload" in event.message_data:
        payload = event.message_data["payload"]

        if payload != {} and ("ignore" in payload):
            return

    if key[0] != "/":
        return

    if key in commands:
        try:
            commands[key].on_message(event, vk)
        except (ValueError, StopIteration):
            send_message(event, vk, message=commands[key].full_help)
    else:
        commands["/help"].on_message(event, vk)


class Command:
    def __init__(self):
        self.help: str = None
        self.full_help: str = None

    def on_message(self, event, vk):
        raise NotImplementedError()


commands = {}
