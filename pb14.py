# checking number is factorial or not
num = int(input("Please enter a number: "))
fact = 1
for i in range(1, num+1):
    fact = fact * i

print(fact)

