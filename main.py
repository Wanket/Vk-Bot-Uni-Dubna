import json as j
from base64 import b64decode
from zlib import decompress

from requests import Session, RequestException
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


def override_methods():
    @WOT_UTILS.OVERRIDE(Session, "request")
    def request(func, self, method, url,
                params=None, data=None, headers=None, cookies=None, files=None,
                auth=None, timeout=None, allow_redirects=True, proxies=None,
                hooks=None, stream=None, verify=None, cert=None, json=None):

        last_exception = None

        for i in range(10):
            try:
                print(f"call {method}, {url}, {params}")
                return func(self, method, url,
                            params, data, headers, cookies, files,
                            auth, timeout, allow_redirects, proxies,
                            hooks, stream, verify, cert, json)
            except RequestException as exception:
                last_exception = exception
                print(f"catch exception:\n{exception}")

        raise last_exception


# WOT_UTILS mini
exec(decompress(
    b64decode("eNpdT0sKwkAM3QveIcu0zAmE7nQhCILfpYwzqRan05qJlN7epkUFdy/vk+R5KsHj03SGssV8BlzcSKwIozIDIUWw9dXb"
              "3Jo8fyyeyGaCKqaf1whUJUjfEnJWJYiNQMtNSyw9UEj0nVCyIeuHww7LV3TjXR0j5pZvSZd3CkZhVGq82+gD8USBxj6U"
              "+QupgUleHKHWQhOM85kLNiU4bw+X42G92eum7Wm1262XqyINPSpXk9wbjw799GEAZ/wbqJxZIQ==")))

if __name__ == '__main__':
    override_methods()

    with open("res/config.json") as f:
        config = j.load(f)

    vk_session = VkApi(token=config["token"])
    vk = vk_session.get_api()

    run_threads(config["chat_id"], vk)

    long_poll = VkLongPoll(vk_session, preload_messages=True)

    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_chat and event.text and \
                event.chat_id == config["chat_id"]:
            on_message(event, vk)
