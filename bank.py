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


quotient = (amount1 + amount2) // 100       # this uses floor division to get the numbers added together divided by 100 without the remainder
remainder = (amount1 + amount2) % 100       # this gets the remainder (i.e. the cents) once the numbers are added together and divided by 100
print(f"The sum of these is €{quotient}.{remainder}") #to print the answer in a legible manner