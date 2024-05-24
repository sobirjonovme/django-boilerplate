import urllib.parse

import requests


class TelegramService:
    def __init__(self, bot_token):
        self.bot_token = bot_token

    def send_message(self, chat_id, text):
        encoded_message = urllib.parse.quote(text)
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

        try:
            response = requests.post(
                url=url,
                params={"chat_id": chat_id, "text": encoded_message, "parse_mode": "HTML"},
            )
            return response.json()
        except Exception as e:
            print(e)
            return None
