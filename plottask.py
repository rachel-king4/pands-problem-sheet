# plottask.py
# this program displays a histogram of normal distribution
# of 1000 values with mean of 5 and standard deviation of 2
# and plots a function as outlined in the code
# Author: Rachel King

import numpy as np
import matplotlib.pyplot as plt

#rando = np.random.randint(100,200,30)
#print(rando)
#np.random.seed(1)
numbers = np.random.normal(loc=5, scale=2, size=1000)    # loc is the mean, scale is the standard deviation

plt.hist(numbers, label="histogram")

x = np.array(range(1,10))
y = x**3

plt.plot(x, y, color='r', label="plot of function")
plt.title("plottask.py")
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.legend()
plt.show()