# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
# 1, 1, 2, 3, 5, 8, 13, …

def fib(n):
    fibonacci = []
    a, b, c = 0, 1, 1
    for x in range(n):
        print(c)
        c = a + b
        a = b
        b = c


n = int(input("length: "))
fib(n)
