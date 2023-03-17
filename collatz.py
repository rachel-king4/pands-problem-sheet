# collatz.py
# This program reads in a positive integer
# and outputs successive values
# it calculates the next value by taking the current value
# and if value is even, divides by two; if value is odd, mulitplies by three and adds one
# author: Rachel King

def amount(message = "Please enter a positive integer: "):
    num = False
    while (not num):
        try:
            num = int(input(message))
        except ValueError:
            print("That was not a number: ",end="")
    return num

number = amount()                           # to prompt user input

while number != 1:                          # while loop keeps the sequence going while number is not 1
    print(number, end=" ")
    if (number % 2) == 0:                   # if number is even, divide it by 2
        number = int(number/2)
    else:
        number = int((number*3) + 1)        # if number is odd, multiply by 3 and add one

print(number)                               # to print the number at the end (one)