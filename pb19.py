str1 = 'ABCD'
str2 = 'PQR'

for i in range(len(str1)):
    print(str1[:i+1] + str2[i:])
