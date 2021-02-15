import smtplib
import os
import datetime as dt
import random
from dotenv import load_dotenv
load_dotenv()

my_email = os.environ.get("GMAIL")
password = os.environ.get("GMAIL_PASS")
receiver_email = os.environ.get("YMAIL")

# Get the current day
current = dt.datetime.now()
day_of_the_week = current.weekday()

# Be sure it's a monday
if day_of_the_week == 0:
    # Get a random quote
    with open("quotes.txt") as quote_data:
        quotes = quote_data.readlines()
        quote = random.choice(quotes)

    # Forward the email containing the quote
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(from_addr=my_email,
                      to_addrs=receiver_email,
                      msg=f"Subject:Weekly Motivation\n\nThis week's quote is {quote}")
