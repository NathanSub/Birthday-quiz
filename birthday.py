"""
birthday.py
Author: Nathan Subrahmanian
Credit: N/A
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
monthnow = month_name[todaymonth]

name = input("What is your name?")
month = input("Which month were you born in?")
year = input("What year were you born in?")
day = input("What day were you born on?")

d=todaydate
m=str(monthnow)
n=str(name)

if day == "31" and month == "October":
    print("You were born on Halloween!")
elif month == m and int(day) == d:
    print("Happy birthday!")

if month == "December" or month == "January" or month == "February":
    if int(year) <= 1980:
        decade == "Stone Age"
    if int(year) >= 1980 and int(year) <= 1990:
        decade == "eighties"
    print("{0},you are a winter baby of the {1}".format(n,decade))
elif month == "March" or month == "April" or month == "May":
    print("{0},you are a spring baby".format(n))
elif month == "June" or month == "July" or month == "August":
    print("{0},you are a summer baby".format(n))
elif month == "September" or month == "October" or month == "November":
    print("{0},you are a fall baby".format(n))