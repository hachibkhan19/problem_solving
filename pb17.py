# Find a max value without using built in function.
from numpy import*
arr = array([5, 3, 2, 6, 7, 12, 9])
max = 0
for i in arr:
    if i > max:
        max = i        
print(max)

