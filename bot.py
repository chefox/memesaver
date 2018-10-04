import sqlite3
import requests

conn = sqlite3.connect("bl.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

offset = 0 # параметр необходим для подтверждения обновления
URL = 'https://api.telegram.org/bot' # URL на который отправляется запрос
TOKEN = '693069318:AAEl-e4U6DBFwXSKy8R_MN13l1SIUGX4l7I' # токен вашего бота, полученный от @BotFather
data = {'offset': 'offset  1', 'limit': 0, 'timeout': 0}

try: # обрабатываем исключения
    request = requests.post(URL+TOKEN+'/getUpdates', data=data) # собственно сам запрос
except:
    print('Error getting updates')

for update in request.json()['result']:
    offset = update['update_id'] #  подтверждаем текущее обновление

    if 'message' not in update or 'text' not in update['message']: # это просто текст или какая-нибудь картиночка?
        print('Unknown message')
        continue

    message_data = { # формируем информацию для отправки сообщения
        'chat_id': update['message']['chat']['id'], # куда отправляем сообщение
        'text': "I'm <b>bot</b>", # само сообщение для отправки
        'reply_to_message_id': update['message']['message_id'], # если параметр указан, то бот отправит сообщение в reply
        'parse_mode': 'HTML' # про форматирование текста ниже
    }
try:
    request = requests.post(URL+TOKEN+'/sendMessage', data=message_data) # запрос на отправку сообщения
except:
    print('Send message error')