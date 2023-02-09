# pands-problem-sheet

References/Comments for bank.py problem:
        I used information from w3schools, https://www.w3schools.com/python/python_string_formatting.asp
        I copied in the code for formatting a value to two decimal places, this ensures if total of both numbers added together had a trailing zero, this trailing zero would be included


References/Comments for pythonaccounts.py problem:
        For the extra problem to modify the program to deal with acc numbers of any length
        I thought that the numbers would be integers and assumed the acc number would be of length greater than 4
        I added an error message to display if the acc number entered by the user was less than 4 digits
        I considered what if there were spaces, so decided to remove the spaces of the user input initially before slicing and replacing
        I used information from your lecture as well as code and info from https://www.codingem.com/remove-spaces-from-string-in-python/ to remove any spaces

        As the slicing of the string to separate the last 4 digits was already covered in my initial program in pythonaccounts.py,
        I sliced the string to separate out everything up to the last 4 digits of the acc number
        To replace these digits I used information and code from https://www.geeksforgeeks.org/python-replace-all-numbers-by-k-in-given-string/ 
        In particular I used the "for if" code to replace the digits with an "X"

        I would like to be able to keep the spaces and only replace the digits with an X, while also keeping any spaces at the end and still displaying the last 4 digits
        For example if acc number was 01 4567 89, the output would be XX XX67 89 (I can do this if there is never a space entered in last 4 digits, but it there is it messes up the code a bit and seems to have an extra X or digit). So I left it to remove the spaces for now and just output an account number of any length greater than 4 with only the last 4 digits showing.
