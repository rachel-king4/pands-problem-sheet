# **pands-problem-sheet** #


This repository stores all of the weekly tasks assigned in the Pands module.

The Pands module was undertaken in the first semester of Higher Diploma in Science in Computing in Data Analytics.

## **Table of Contents** ##

 - [Helloworld](#helloworld)
 - [Bank](#bank)
 - [Accounts](#accounts) 
 - [Collatz](#collatz)
 - [Weekday](#weekday)
 - [Squareroot](#squareroot)
 - [Es](#es)
 - [Plottask](#plottask)


## **Helloworld** ##


```
Commit and push a file to the problem sheet called helloworld.py
This file should contain a python program that displays Hello World! when it is run
```

This program contains one line of code, which simply uses the print function to print the string "Hello World!"


## **Bank** ##


```
Write a program called bank.py 

The program should:

Prompt the user and read in two money amounts (in cent)
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
```

This program uses the input function to prompt the user to input two money amounts in cents.
It then uses a mathematical formula to add them together and outputs the calculated amount in the format euros and cents with a decimal point and the € sign.
This required some formatting to be applied to the output calulation.

The output was also formatted to display the amount to two decimal places, as this is the way funds are typically displayed.

I used information from w3schools, https://www.w3schools.com/python/python_string_formatting.asp . I copied in the code for formatting a value to two decimal places, this ensures if total of both numbers added together had a trailing zero, this trailing zero would be included.


## **Accounts** ##


```
Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)
```

This program prompts the user for input of an account number. It contains error handling to account for the user entering something other that a number.

The code then converts the number to a string for the purpose of slicing. It then slices the string to separate the last 4 digits and then prints out 6 X's along with the sliced string containing the last 4 digits.

```
Modify the program to deal with account numbers of any length
```

This program again prompts the user for input of an account number. This time it deals with account numbers of any length. It contains error handling to account for the user entering something other that a number.

I thought that the numbers would be integers and assumed the account number would be of length greater than 4.

The code then converts the number to a string for the purpose of slicing. It slices the string to separate the last 4 digits and then slices the string to separate out everything up to the last 4 digits of the account number. To replace these digits I used information and code from https://www.geeksforgeeks.org/python-replace-all-numbers-by-k-in-given-string/ . In particular I used the "for if" code to replace the digits with an "X"


## **Collatz** ##


```
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.
```
This program prompts user input of a positive integer. It contains error handling for any p=input by the user that is not a number.

I used a while loop to keep running the code until the number reached 1. The code first checks is the number is odd or even with the if and else statements, if the number is even it does a mathematical operation, if the number is odd it does a different mathematical operation.

I used information from the lecture videos to run the while loop (eg while number != 1 do something, then once number reached one, stop) and to get the output to print on one line, with a space in between each number.


## **Weekday** ##


```
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
```

This program imports the datetime module in order to perform operations on the date and time.

The date is imported and the date.weekday() assigns integers 0 to Monday, 1 to Tuesday and so on. These integers are then used to tell the the computer what to do in the for loop.
The program was ran on both a weekday and a weekend in order to be sure the program works as expected.


I used informaton and code from Stack Overflow to solve this problem.
 https://stackoverflow.com/questions/45870820/how-to-check-if-today-is-monday-in-python is the specific link i took the code from.

## **Squareroot** ##


```
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called sqrt that does this.
```

My intital research into this problem involved researching what Newton's Method for approximating square roots.

In this method:
* N is any number, the square root of N can be given by the formula: 
            root = 0.5 * (X + (N / X)) 
* X is any assumed square root of N and root is the correct square root of N

In this program, a while loop is used to iterate the method over and over until the required tolerance has been reached. I set the tolerance to be 0.0001, so it will stop once the differnece between the assumed root and the correct root is less than 0.0001.

It then formats the answer to one decimal place and prints it out. 

I used information from the lecture about functions and code from https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ to solve this problem.


## **Es** ##


```
Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.

The program should take the filename from an argument on the command line.
```

The program reads the file, and uses the built-in count method with the argument as the letter "e" to count the number of times "e" appears in the txt file and diplays the count of the letter "e".

Open (FILENAME, 'r') opens the file in read format, which is sufficient for the purpose of this program.

To enable the text file to be called from the command line, the sys module was imported.

I used https://www.gutenberg.org/files/2701/old/moby10b.txt to get the moby_dick.txt file - I created a moby_dick.txt file and copied & pasted the text from this link.

I used code from https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/ which counts the number of times a letter appears in a text file in Python.

I then used code from https://askubuntu.com/questions/1059579/input-the-filename-in-the-commandline-as-an-argument-in-python to enable the program to take the filename from an argument on the command-line.
* sys.agv is a list of all the command-line arguments passed to the script
* sys.argv[1] contains the first command-line argument passed to the script



## **Plottask** ##


```
Write a program called plottask.py that displays:

- a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
- and a plot of the function  h(x)=x3 in the range [0, 10], 

on the one set of axes.
```

This program imports the numpy and matplotlib modules.
The random function from numpy was used to generate 1000 random values, which had a mean of 5 and standard deviation of 2.
A histogram of normal distribution of these values was plotted.

The function h(x)= x^3 was also plotted in the range 0-10.

Formatting was applited to the plot including adding a title, labels for the axes, and a legend.

I used information from the lecture videos for week 08 and from Stack Overflow (https://stackoverflow.com/questions/70937689/plotting-multiple-line-graphs-in-matplotlib) for inspiration for the program plottask.py

The plot is saved to the same directory, and looks like this:

![plottask.py output](https://github.com/rachel-king4/pands-problem-sheet/blob/main/plottask.png)
