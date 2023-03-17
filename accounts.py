# accounts.py
# This program reads in a 10 character account amount
# outputs acc number with only last 4 digits showing (and first 6 as Xs)
# author: Rachel King

def amount(message = "Please enter a 10 digit account number: "):
    num = False
    while (not num):
        try:
            num = int(input(message))
        except ValueError:
            print("That was not a number: ",end="")
    return num

account_number = str(amount())
secure_display_acc_number = account_number[-4:]  # this slices the string to separate the last 4 digits

# to print masked acc number
print(f"XXXXXX{secure_display_acc_number}")



# modified to deal with acc numbers of any length
# assumed number is positive and an integer, also assumed account number has more than 4 digits
# what if account number has spaces

def amount2(message = "Please enter an account number: "):
    num = False
    while (not num):
        try:
            num = int(input(message))
        except ValueError:
            print("That was not a number: ",end="")
    return num

account_number2 = str(amount2())
no_spaces = account_number2.replace(" ", "")  # this is to remove any spaces and ensure 4 digits are displayed at the end
secure_display_acc_number2 = no_spaces[-4:]   # this slices the string to separate the last 4 digits

# to mask all digits except last 4
# slice account number for all digits up to last 4
# and replace all digits with an X

replaced_numbers_in_account = no_spaces[:-4]
for number in replaced_numbers_in_account:
    if number.isdigit():
        replaced_numbers_in_account = replaced_numbers_in_account.replace(number, "X")

print(f"{replaced_numbers_in_account}{secure_display_acc_number2}")
