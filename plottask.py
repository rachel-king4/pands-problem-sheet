# plottask.py
# this program displays a histogram of normal distribution
# of 1000 values with mean of 5 and standard deviation of 2
# and plots a function as outlined in the code
# Author: Rachel King

import numpy as np
import matplotlib.pyplot as plt

#np.random.seed(1)
numbers = np.random.normal(loc=5, scale=2, size=1000)    # loc is the mean, scale is the standard deviation

plt.hist(numbers, label="histogram")    # this creates a histogram plot of a normal distribution of 1000 values with mean of 5 and standard deviation of 2

x = np.array(range(0,10))   # this sets the range of x from 0 to 9
y = x**3                    # to set y = x cubed

plt.plot(x, y, color='r', label="h(x) = x^3") # this plots the function y = x cubed
plt.title("plottask.py")                            # this adds the title
plt.xlabel("X-axis data")                           # this adds a label to x axis
plt.ylabel("Y-axis data")                           # this adds a label to y axis
plt.legend()                                        # this adds a legend to the plot
plt.xlim([0, 10])                      # this sets the x axis to display from 0-10 only
plt.savefig("plottask.png")            # this saves the plot as a figure in the same folder