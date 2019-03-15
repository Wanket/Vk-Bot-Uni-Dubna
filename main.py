import json

from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType

from command.Command import on_message
from threads.NextDay import NextDay
from threads.NextDayHomework import NextDayHomework
from threads.NextLesson import NextLesson
from threads.SyncSchedule import SyncSchedule


def run_threads(chat_id, vk_api):
    NextDay().start()
    NextDayHomework(chat_id, vk_api).start()
    NextLesson(chat_id, vk_api).start()
    SyncSchedule().start()


if __name__ == '__main__':
    with open("res/config.json") as f:
        config = json.load(f)

    vk_session = VkApi(token=config["token"])
    vk = vk_session.get_api()

    run_threads(config["chat_id"], vk)

    long_poll = VkLongPoll(vk_session, preload_messages=True)

    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_chat and event.text and \
                event.chat_id == config["chat_id"]:
            on_message(event, vk)
