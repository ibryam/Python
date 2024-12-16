import smtplib
import time

import requests

MY_EMAIL = "ibryamfaik1991@gmail.com"
MY_PASSWORD = "wkitldkmudvbydfg"

api_key = "myapikey"
city_name = "Kardzhali"

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": 41.642836,
    "lon": 25.353773,
    "appid": api_key,
    "cnt": 4
}
response = requests.get(endpoint, params= params)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Rain scanner!\n\n RAIN TODAY!")
else:
    print(f"Today is going to be a good day in Kardzhali!")