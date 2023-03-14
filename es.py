# es.py
# this program reads in a text file and outputs the number of e's in it
# Author: Rachel King

import sys
FILENAME = sys.argv[1]                  # this ensures the program takes the filename from an argument on the command line

# explicit function to return the letter count
def letter_frequency(FILENAME, letter):
    # open file in read mode
    with open(FILENAME, 'r') as f:
        data = f.read()
 
    # using count()
        return data.count(letter)
 
 
# call the function and display the letter count
print(letter_frequency(FILENAME, 'e'))