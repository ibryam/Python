import requests

TELEGRAM_CHAT_ID = "5290548584"
TELEGRAM_TOKEN = "7782718578:AAHjvQgO3BmHxGUqXo2eOF5FWtBEF1mTIhY"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.



    def send_telegram_message(self, message):
        parameters = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
        }

        response = requests.post(url=f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
                                 params=parameters)
        response.raise_for_status()
        data = response.json()
        return data