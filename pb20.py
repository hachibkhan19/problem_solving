# Count number of even and odd value.
def fun(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd

lst = [2, 3, 4, 5, 6, 7, 8, 9]
even, odd = fun(lst)
print(even)
print(odd)
