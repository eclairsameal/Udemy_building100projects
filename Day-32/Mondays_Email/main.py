import smtplib
import datetime as dt
import random

g_email = ""
g_password = ""

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt", "r") as file:
        data = file.readlines()
    word = random.choice(data)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=g_email, password=g_password)
        connection.sendmail(
            from_addr=g_email,
            to_addrs=g_email,
            msg=f"Subject:Monday Motivation\n\n{word}")





