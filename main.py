import time

import requests

from config import TOKEN


class Bot:
    
    def __init__(self, token: str):
        self.BASE_URL = F'https://api.telegram.org/bot{token}'
        self.offset = None

    def get_me(self) -> dict:
        get_me_url = f'{self.BASE_URL}/getMe'
        
        response = requests.get(get_me_url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Telegram server xatolik qaytardi!')

    def get_updates(self) -> list[dict]:
        get_updates_url = f'{self.BASE_URL}/getUpdates'
        
        params = {
            'offset': self.offset,
            'limit': 20
        }
        response = requests.get(get_updates_url, params=params)

        if response.status_code == 200:
            return response.json()['result']
        else:
            raise Exception('Telegram server xatolik qaytardi!')
        
    def send_message(self, chat_id: str, text: str) -> None:
        send_message_url = f'{self.BASE_URL}/sendMessage'
        
        params = {
            'chat_id': chat_id,
            'text': text
        }
        requests.get(send_message_url, params=params)

    def send_photo(self, chat_id: str, photo: str) -> None:
        pass

    def start_polling(self) -> None:
        
        while True:
            updates = self.get_updates()
            time.sleep(1)

            for update in updates:
                message = update.get('message')
                if message:
                    text = message.get('text')
                    if text:
                        self.send_message(
                            chat_id=message['chat']['id'],
                            text=text
                        )

                self.offset = update['update_id'] + 1


bot = Bot(TOKEN)
bot.start_polling()
