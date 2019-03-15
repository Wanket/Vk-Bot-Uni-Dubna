from api import send_message
from command.Command import Command


class AbstractSchedule(Command):
    def on_message(self, event, vk):

        spl = event.text.split()
        if len(spl) < 2:
            send_message(event, vk, message=self.full_help)
        elif spl[1] == "добавить" or spl[1] == "изменить":
            self.update(event, vk, spl)
        elif spl[1] == "удалить":
            self.delete(event, vk, spl)
        elif spl[1] == "показать":
            self.show(event, vk, spl)
        else:
            send_message(event, vk, message=self.full_help)

    def update(self, event, vk, spl):
        raise NotImplementedError()

    def delete(self, event, vk, spl):
        raise NotImplementedError()

    def show(self, event, vk, spl):
        raise NotImplementedError()
