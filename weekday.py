# weekday.py
# This program outputs whether or not today is a weekday
# author: Rachel King

from datetime import date

if date.today().weekday() < 5:                          # Days of the week are assigned numbers: Monday = 0, Tuesday = 1, and so on
    print("Yes, unfortuantely today is a weekday")      # weekdays (monday-friday) are therefore numbers 0-4 and weekends are umbers 5 and 6
else:
    print("It is the weekend, yay!")

