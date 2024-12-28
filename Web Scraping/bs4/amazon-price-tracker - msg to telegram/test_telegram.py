import requests

from notification_manager import NotificationManager, TELEGRAM_CHAT_ID


notify = NotificationManager()
#

notify.send_telegram_message(message)
