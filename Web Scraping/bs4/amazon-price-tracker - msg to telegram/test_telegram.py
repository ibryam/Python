import requests

from notification_manager import NotificationManager, TELEGRAM_CHAT_ID


message = "madafaka first free message"

notify = NotificationManager()
#

notify.send_telegram_message(message)
