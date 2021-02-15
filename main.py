import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


my_email = os.environ.get("YMAIL")
password = os.environ.get("YMAIL_pass")
receiver_email = os.environ.get("GMAIL")

with smtplib.SMTP("smtp.mail.yahoo.com") as conn:
    conn.starttls()
    conn.login(user=my_email, password=password)
    conn.sendmail(from_addr=my_email,
                  to_addrs=receiver_email,
                  msg="Subject:Hello G\n\nBody oby of the awesome type.")
