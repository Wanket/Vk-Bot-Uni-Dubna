import pickle


class Message:
    def __init__(self, event):
        self.payload = {}
        if "payload" in event.message_data:
            self.payload = event.message_data["payload"]

        self.reply_to = ""
        if "reply_message" in event.message_data:
            self.reply_to = event.message_data["reply_message"]["id"]

        self.attachments = ""
        self.forward_messages = ""
        self.text = event.text

        for forward_message in event.message_data["fwd_messages"]:
            self.forward_messages += f"{forward_message['id']},"

        for attachment in event.message_data["attachments"]:
            send_attachment = ""

            type_attachment = attachment["type"]

            if type_attachment == "link":
                continue

            if type_attachment == "wall":
                send_attachment += f"wall{attachment['wall']['from_id']}_{attachment['wall']['id']}"
            else:
                send_attachment += f"{type_attachment}{attachment[type_attachment]['owner_id']}_" \
                    f"{attachment[type_attachment]['id']}"

            if "access_key" in attachment[type_attachment]:
                send_attachment += f"_{attachment[type_attachment]['access_key']}"

            self.attachments += f"{send_attachment},"

    def is_empty(self, command):
        return self.text == command and self.is_empty_except_text()

    def is_empty_except_text(self):
        return self.reply_to == "" and self.forward_messages == "" and self.attachments == ""

    def dump(self):
        return pickle.dumps(self)

    @staticmethod
    def load(message_bytes):
        return pickle.loads(message_bytes)
