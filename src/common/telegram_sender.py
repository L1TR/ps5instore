import requests
from common.config import TELEGRAM_TOKEN, TELEGRAM_CHATID

class TelegramSender(object):
    def __init__(self):
        self.token = TELEGRAM_TOKEN
        self.chatId = TELEGRAM_CHATID

    def send(self, log):
        send_url = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + self.chatId + '&parse_mode=Markdown&text=' + log
        response = requests.get(send_url)
        return response.json()