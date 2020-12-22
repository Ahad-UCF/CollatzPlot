# Ahad Bawany
# A simple project to check How long numbers take to tend to 1 with Collatz Sequences

## Import useful libraries
import numpy as np
import matplotlib.pyplot as plt

# Simple Code for the Collatz Sequence
def collatz(n, i):
    if n == 1:
        return i
    if n % 2 == 0:
        return collatz(n//2, i + 1)
    elif n % 2 != 0:
        return collatz(3 * n + 1, i + 1)

# Grab how many iterations it takes for the Collatz to tend towards 1
# Populate list for values for 1 through 100
colList = []
for i in range(1, 101, 1):
    colList.append(collatz(i, 0))

plt.plot(colList)
plt.xlabel('input number')
plt.ylabel('iterations to get to 1')
plt.show()
