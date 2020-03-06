# insert a value into from user and searching a value
from array import*
array_length = int(input("Enter the length of array: "))
arr = array('i', [])

for i in range(array_length):
    value = int(input("Enter the value: "))
    arr.append(value)

print(arr)

pos = 0
search_element = int(input("Enter the searching value: "))
for j in arr:
    if j == search_element:
        print("Found", pos+1)
        break
    pos += 1

else:
    print("Not found")

