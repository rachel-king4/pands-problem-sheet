# bank.py
# This program reads in two amounts, adds them together
# and prints them out in readable format with € sign and decimal point between the euro and cent
# author: Rachel King


amount1 = int(input("Enter amount1(in cent):"))
amount2 = int(input("Enter amount2(in cent):"))
total = (amount1 + amount2)/100
txt = "The sum of these is €{:.2f}"
print(txt.format(total))