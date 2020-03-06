# Solving a fibonacci sequence
a = 0
b = 1
print(a)
print(b)

for i in range(1, 51):
    a, b = b, a + b
    if b > 50:
        break
    print(b)

