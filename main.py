import requests

from config import TOKEN


class Bot:
    
    def __init__(self, token: str):
        self.BASE_URL = F'https://api.telegram.org/bot{token}'

    def get_me(self) -> dict:
        get_me_url = f'{self.BASE_URL}/getMe'
        
        response = requests.get(get_me_url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Telegram server xatolik qaytardi!')

    def get_updates(self) -> list[dict]:
        get_updates_url = f'{self.BASE_URL}/getUpdates'
        
        response = requests.get(get_updates_url)

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


bot = Bot(TOKEN)
bot.send_message(chat_id=1258594598, text='hi')
