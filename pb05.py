# checking which number is greatest.
value1 = int(input("Please enter a 1st value: "))
value2 = int(input("Please enter a 2nd value: "))
value3 = int(input("Please enter a 3rd value: "))

if value1 > value2 and value1 > value3:
    print(value1, "is greatest.")
elif value2 > value1 and value2 > value3:
    print(value2, "is greatest")
elif value1 == value2 and value1 == value3:
    if value2 == value1 and value2 == value3:
        if value3 == value1 and value3 == value2:
            print("All values are same, please try again.")
else:
    print(value3, "is greatest")
