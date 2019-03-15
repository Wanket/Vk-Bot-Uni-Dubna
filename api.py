def send_message(event, vk, **kwargs):
    vk.messages.send(
        chat_id=event.chat_id,
        random_id=0,
        payload='{"ignore":true}',
        **kwargs)
