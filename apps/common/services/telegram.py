import urllib.parse

import requests


def send_telegram_message(bot_token, chat_id, text):
    encoded_message = urllib.parse.quote(text)
    url = (
        f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={encoded_message}&parse_mode=HTML"
    )
    response = requests.post(url)
    return response.json()
