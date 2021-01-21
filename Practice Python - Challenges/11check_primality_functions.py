# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
from math import sqrt

n = int(input("number: "))

for x in range(2, int(sqrt(n))):
    if n % x == 0:
        print("Not a prime")
        exit()
print("Prime")
