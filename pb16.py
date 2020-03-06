# Adding two array using for loop.
from numpy import*

arr1 = array([4, 3, 1, 4, 6])
arr2 = array([5, 3, 2, 4, 2])

for i in range(len(arr1)):
    add = arr1[:] + arr2[:]

print(add)

