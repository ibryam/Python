import smtplib
import datetime as dt
import random

MY_EMAIL = "ibryamfibryam@gmail.com"
MY_PASSWORD = "zzxxzz" #change password

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1: #if it's Tuesday
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{quote}")

