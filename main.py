
import csv
import random
import smtplib
from datetime import datetime
import pandas
MY_EMAIL = "Your Mail"
PASSWORD = "Your Gmail App password"

# Get today's date
today = (datetime.now().month,datetime.now().day)

# Create a dictionary from birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthday_dic = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dic:
    birthday_person = birthday_dic[today]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_feild:
        content = letter_feild.read()
        content = content.replace("[NAME]", birthday_person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birth Day\n\n{content} ")



