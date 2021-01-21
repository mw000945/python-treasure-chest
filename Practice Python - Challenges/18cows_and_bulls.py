# https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
from random import randint

num = str(randint(1000, 9999))
print("Welcome to the Cows and Bulls Game!")

guesses = 0
while True:
    cows = 0
    bulls = 0
    user = str(input("Enter a number (4-digit): "))
    guesses += 1
    if user == num:
        print(f"It took you {guesses} guesses to find the number: {num}")
        exit()
    for d in user:
        if d in num:
            if num.index(d) == user.index(d):
                cows += 1
            else:
                bulls += 1
    print(f"Cow(s): {cows} Bull(s): {bulls}")
