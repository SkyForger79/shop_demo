import requests
import json

urlTelegramgetMe = "https://api.telegram.org/bot560754292:AAGQ3aTUK9p1LcUXuVPIZTiUewzGi1Kf5-4/getMe"
responce = requests.get(urlTelegramgetMe)
# форматируем json в словарь

decoded = responce.json()

bot_result = decoded['result']
bot_id = bot_result['id']

# также можем сделать это сразу
bot_id = decoded['result']['id']

print(bot_id)

def get_bot_updates(limit, offset):
    url = "https://api.telegram.org/bot560754292:AAGQ3aTUK9p1LcUXuVPIZTiUewzGi1Kf5-4/getUpdates"
    
    # записываем параметры в словарь
    par = {'limit': limit, 'offset': offset} 
    result = requests.get(url, params=par)

    # форматируем json в словарь
    decoded = result.json()
    return decoded['result']
    
result = get_bot_updates(5,0)

# получаем текст сообщения
first_update = result[0]

message = first_update['message']

# также можем это сделать в одну строку
text = result[0]['message']['text']
message_id = result[0]['message']['message_id']

new_offset = message_id + 1

# выводим текст сообщения и отмечаем прочитанным
print(message_id, text)
get_bot_updates(5, new_offset)

for item in result:
    text = item['message']['text']
    message_id = item['message']['message_id']
    print(message_id, text)