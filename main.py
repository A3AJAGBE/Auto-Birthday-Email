import datetime as dt
import pandas as pd
import random

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
        print(letter)


