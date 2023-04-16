# squareroot.py
# This program takes a postiive floating point number as input
# and outputs an approximation of its square root
# author: Rachel King

def sqrt(n) :
    # Assuming the sqrt of n as n only
    x = n
    # To count the number of iterations
    count = 0
    while (1) :
        count += 1
        # Calculate estimate
        root = 0.5 * (x + (n / x))
        # Check for closeness                   # this is to set how accurate we want the result to be
        if (abs(root - x) < 0.0001) :           # it's set to be accurate within 0.0001 
            break
        # Update root
        x = root
    return root
def amount(message = "Please enter a postive number: "):
    num = False
    while (not num):
        try:
            num = float(input(message))
        except ValueError:
            print("That was not a number: ",end="")
    return num
n = amount()
answer = float(sqrt(n))
answer_rounded = "{:.1f}".format(answer)
print(f"The square root of {n} is approx. {answer_rounded}")