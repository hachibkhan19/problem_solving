#from sys import argv

#a = int(argv[1])
#b = int(argv[2])

#print(a+b)

#char = input("Please enter a char: ")[0]
#print(char[1])
#print(char)

#expr = eval(input("Please enter a expression: "))
#print(expr)
#from array import*

#arr = array('i', [2, 3, 4, 5])
#newarr = array(arr.typecode, (a for a in arr))
#print(newarr)

#from numpy import*

#arr = array([2, 3, 4, 5])

#print(size(arr))

from numpy import*

#arr = array([2, 3, 4])
#arr = linspace(1, 15, 15)
#arr = arange(1, 10, 3)
#arr = ones(5, int)
#arr = zeros(5)
#arr = logspace(2, 10, 2)

#arr = array([4, 2, 3, 4, 5])
#arr1 = array([4, 2, 3, 4, 5])
#arr2 = arr + arr1
#print(arr2)
#new = arr.copy()
#add = arr + 5
#print(add)
#new = arr.view()
#new[0] = 8
#print(arr)
#print(new)


arr = array([4, 2, 3, 4, 2, 3, 4, 5])


arr1 = arr.reshape(4, 2)
arr3 =arr1.flatten()
print(arr3)
print(arr1)
print(arr.size)
print(arr1.ndim)
print(arr.shape)



