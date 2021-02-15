import smtplib
import os
import datetime as dt
import pandas as pd
import random

from dotenv import load_dotenv
load_dotenv()

# Default email information
my_email = os.environ.get("GMAIL")
password = os.environ.get("GMAIL_PASS")

# Get the current day and month
current = dt.datetime.now()
day = current.day
month = current.month
today = (day, month)

# The day and month in the birthday information
data = pd.read_csv("birthday_information.csv")
data_dict = {(row['day'], row['month']): row for (index, row) in data.iterrows()}

PLACEHOLDER = "[NAME]"

# Check if someone's birthday is today
if today in data_dict:
    # Get the person
    person = data_dict[today]
    # Select a random letter template
    num = random.randint(1, 3)
    letter_template = f"letterTemplates/letter{num}.txt"

    # Open the letter
    with open(letter_template) as template:
        content = template.read()
        # Replace the placeholder with the person's name
        letter = content.replace(PLACEHOLDER, person['name'])

        # Get a random quote
        with open("quotes.txt") as quote_data:
            quotes = quote_data.readlines()
            quote = random.choice(quotes)

        # Send the birthday email
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=my_email, password=password)
            conn.sendmail(from_addr=my_email,
                          to_addrs=person['email'],
                          msg=f"Subject:Happy Birthday {person['name']}!!!\n\n{letter}\n{quote}")

