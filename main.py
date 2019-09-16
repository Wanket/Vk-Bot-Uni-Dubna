import json as j

from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType

from message import on_message

if __name__ == '__main__':

    with open("res/config.json") as f:
        config = j.load(f)

    vk_session = VkApi(token=config["token"])
    vk = vk_session.get_api()

    long_poll = VkLongPoll(vk_session, preload_messages=True)

    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_chat and event.text and \
                event.chat_id == config["chat_id"]:
            on_message(event, vk)
