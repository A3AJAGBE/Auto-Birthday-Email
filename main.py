import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


my_email = os.environ.get("GMAIL")
password = os.environ.get("GMAIL_PASS")
receiver_email = os.environ.get("YMAIL")

conn = smtplib.SMTP("smtp.gmail.com")
conn.starttls()
conn.login(user=my_email, password=password)
conn.sendmail(from_addr=my_email,
              to_addrs=receiver_email,
              msg="Testing python smtp connections")
conn.close()
