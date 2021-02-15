import datetime as dt
import pandas as pd

# Get the current day and month
current = dt.datetime.now()
day = current.day
month = current.month
today = (day, month)

# The day and month in the birthday information
data = pd.read_csv("birthday_information.csv")
data_dict = {(row['day'], row['month']): row for (index, row) in data.iterrows()}



