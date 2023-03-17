# bank.py
# This program reads in two amounts, adds them together
# and prints them out in readable format with € sign and decimal point between the euro and cent
# author: Rachel King


def amount(message = "Enter amount1(in cent): "):
    num = False
    while (not num):
        try:
            num = int(input(message))
        except ValueError:
            print("That was not a number: ",end="")
    return num

amount1 = amount()
amount2 = amount("Enter amount2(in cent): ")

total = (amount1 + amount2)/100
txt = "The sum of these is €{:.2f}"
print(txt.format(total))