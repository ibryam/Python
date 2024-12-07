import requests
from datetime import datetime as dt
import smtplib
import time

MY_EMAIL = "ibryamfaik1991@gmail.com"
MY_PASSWORD = "zzzzxxxxx"
MY_LAT = 43.200687   # use 52.478858 for wexstrasse 13
MY_LNG =  27.914113  # use 13.336168 for wexstrasse 13

LAVI_LAT = 52.478858
LAVI_LNG = 13.336168

def is_iss_overhead():
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = data["iss_position"]["longitude"]
    iss_latitude = data["iss_position"]["latitude"]

    iss_position = (iss_longitude, iss_latitude)

    # My position is within +5 or -5 degrees of the iss position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: LOOK 👆👆🛰️🛰️🛰️🛰️\n\n THE ISS IS ABOVE YOU IN THE SKY.")
