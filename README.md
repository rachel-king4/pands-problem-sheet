# **pands-problem-sheet**

### **References/Comments for bank.py problem:**
#
I used information from w3schools, https://www.w3schools.com/python/python_string_formatting.asp . I copied in the code for formatting a value to two decimal places, this ensures if total of both numbers added together had a trailing zero, this trailing zero would be included


### **References/Comments for accounts.py problem:**
#
For the extra problem to modify the program to deal with acc numbers of any length. I thought that the numbers would be integers and assumed the acc number would be of length greater than 4. I added an error message to display if the acc number entered by the user was less than 4 digits. I considered what if there were spaces, so decided to remove the spaces of the user input initially before slicing and replacing. I used information from your lecture as well as code and info from https://www.codingem.com/remove-spaces-from-string-in-python/ to remove any spaces

As the slicing of the string to separate the last 4 digits was already covered in my initial program in pythonaccounts.py, I sliced the string to separate out everything up to the last 4 digits of the acc number. To replace these digits I used information and code from https://www.geeksforgeeks.org/python-replace-all-numbers-by-k-in-given-string/ . In particular I used the "for if" code to replace the digits with an "X"

I would like to be able to keep the spaces and only replace the digits with an X, while also keeping any spaces at the end and still displaying the last 4 digits. For example if acc number was 01 4567 89, the output would be XX XX67 89 (I can do this if there is never a space entered in last 4 digits, but it there is it messes up the code a bit and seems to have an extra X or digit). So I left it to remove the spaces for now and just output an account number of any length greater than 4 with only the last 4 digits showing.


### **References/Comments for collatz.py problem:**
#
For this, I used a while loop to keep running the code until the number reached 1. I used information from the lecture videos to run the while loop (eg while number != 1 do something, then once number reached one, stop)


### **References/Comments for weekday.py problem:**
#
I used informaton and code from Stack Overflow to solve this problem.
 https://stackoverflow.com/questions/45870820/how-to-check-if-today-is-monday-in-python is the specific link i took the code from.
 
 The date is imported and the date.weekday() assigns integers 0 to Monday, 1 to Tuesday and so on. These integers are then used to tell the the computer what to do in the for loop.

### **References/Comments for squareroot.py problem:**
#
I used information from Andrew's lecture about functions and code from https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ to solve this problem.

I researched Newton's Method for approximating square roots.

In this method:
* N is any number, the square root of N can be given by the formula: 
            root = 0.5 * (X + (N / X)) 
* X is any assumed square root of N and root is the correct square root of N

A while loop is used to iterate the method over and over until the required tolerance has been reached. I set the tolerance to be 0.0001, so it will stop once the differnece between the assumed root and the correct root is less than 0.0001.

It then formats the answer to one decimal place and prints it out.


### **References/Comments for es.py problem:**
#
I used https://www.gutenberg.org/files/2701/old/moby10b.txt to get the moby_dick.txt file - I created a moby_dick.txt file and copied & pasted the text from this link.

I used code from https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/ which counts the number of times a letter appears in a text file in Python.

The program reads the file, and uses the built-in count method with the argumentas the letter "e" to count the number of times "e" appears in the txt file and diplays the count of the letter "e".

I then used code from https://askubuntu.com/questions/1059579/input-the-filename-in-the-commandline-as-an-argument-in-python to enable the program to take the filename from an argument on the command-line.
* sys.agv is a list of all the command-line arguments passed to the script
* sys.argv[1] contains the first command-line argument passed to the script