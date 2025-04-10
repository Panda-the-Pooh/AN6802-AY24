import requests
import time

TOKEN = 'TELEGRAM_BOT_TOKEN'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'

# 用于记录哪些用户已经退出
terminated_users = set()

def get_updates(offset=None):
    url = BASE_URL + 'getUpdates'
    if offset:
        url += f'?offset={offset}'
    response = requests.get(url)
    return response.json()

def send_message(chat_id, text):
    url = BASE_URL + f'sendMessage?chat_id={chat_id}&text={text}'
    requests.get(url)

def main():
    last_update_id = None
    while True:
        updates = get_updates(offset=last_update_id)
        if "result" in updates and updates["result"]:
            for item in updates["result"]:
                last_update_id = item["update_id"] + 1
                message = item.get("message")
                if not message:
                    continue

                chat_id = message["chat"]["id"]
                text = message.get("text", "")

                if chat_id in terminated_users:
                    # 如果用户已经退出，就不再响应
                    continue

                if text.lower() == "exit":
                    send_message(chat_id, "Conversation ended.")
                    terminated_users.add(chat_id)
                elif text.isnumeric():
                    prediction = float(text) * 100 + 10
                    send_message(chat_id, f"Your predicted value is {prediction}")
                    send_message(chat_id, "Enter another number or type 'exit' to end.")
                else:
                    send_message(chat_id, "Please enter a valid number or type 'exit'.")

        time.sleep(2)

if __name__ == "__main__":
    main()