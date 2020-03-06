# fibonacci sequence
def fibo(n):

    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)        
        print(b)

        for i in range(2, n):
            a, b = b, a + b
            print(b)

fibo(10)

