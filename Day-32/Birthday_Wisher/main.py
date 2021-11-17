##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import glob
import random
import smtplib

g_email = ""
g_password = ""

# 1. Update the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")
# print(birthdays)
glob_letter_file = glob.glob("letter_templates/letter_*.txt")
# print(glob_letter_file)
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
now_day = now.day
now_month = now.month

for birthday in birthdays:
    if birthday["month"] == now_month and birthday["day"] == now_day:
        choice_file = random.choice(glob_letter_file)
        with open(choice_file, "r") as file:
            # print(file.read())
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
            email_meg = file.read().replace("[NAME]", birthday["name"])
            #print(email_meg)
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=g_email, password=g_password)
            connection.sendmail(
                from_addr=g_email,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy birthday!\n\n{email_meg}")




