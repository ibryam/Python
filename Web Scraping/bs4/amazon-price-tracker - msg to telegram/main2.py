from bs4 import BeautifulSoup
import requests
import smtplib
import os
from notification_manager import NotificationManager
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


notify = NotificationManager()
#

# Practice
# url = "https://appbrewery.github.io/instant_pot/"
# Live Site
url = "https://www.amazon.de/-/en/Peak-Design-Travel-Backpack-Black/dp/B07GH4PBWM?crid=2JMBRHYSK3E1H&dib=eyJ2IjoiMSJ9.KC17WrpI5WZb-i9TiBX67hy2ebqDwDPvQie_VGz_0KIY0WDDZ9fwzE-2pcqMOoQrW1AMUojn_GMy_T9mPbofAt4WaSMkqy8Q2tmnwxxPlr4tl6iQ5tJCcqewqLo_Z0k7DNHc53cOiG-ixE7ccd8cSg_CgMXIfon5lsWNiWVKNfZGfBaugndctGicxFbTEwQjGb-dOvwL9A9wAf2SNxMfiH7cLuunxO2O7e4Qnel69KqQyvPvqYg7pQE5TB8tLqzdG0t7V5-tsV57kc5ZJR5qtFdSWo9AHHYupoGSH5Gl_ck5qeFWvQv3br-0944yHyjzyzEP0Yx2_-oNK56ACrDuonv2rKqCh_VGKmr4lx8TRLic73ZYWsoK-GCbKwVd8TGB-LHM060BknDz19dHH4ABOqmbZ_ak5KXXj7hyt0yM0BnS1frl8VldtMUgHpISA9Ms.ex0YNoHb5v7ecG7YT49m_L5AOIrZo_KxyLxUemvs1ZM&dib_tag=se&keywords=peak+design+45&nsdOptOutParam=true&qid=1735391731&sprefix=%2Caps%2C121&sr=8-1"

# ====================== Add Headers to the Request ===========================

# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
#     "Dnt": "1",
#     "Priority": "u=1",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
# }

# A minimal header:

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,bg;q=0.8,tr;q=0.7"
}

# Adding headers to the request
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# Check you are getting the actual Amazon page back and not something else:
print(soup.prettify())

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()

# Remove the dollar sign using split
price_without_currency = price.split("$")[1]

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 10000

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    # ====================== Send the telegram message ===========================

    notify.send_telegram_message(message)

    # # ====================== Send the email ===========================
    #
    # with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
    #     connection.starttls()
    #     result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
    #     connection.sendmail(
    #         from_addr=os.environ["EMAIL_ADDRESS"],
    #         to_addrs=os.environ["EMAIL_ADDRESS"],
    #         msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
    #     )