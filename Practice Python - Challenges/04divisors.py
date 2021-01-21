# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
n = int(input("number: "))
for x in range(1, n):
    if n % x == 0:
        print(x)

# will think of a more adequate solution later
