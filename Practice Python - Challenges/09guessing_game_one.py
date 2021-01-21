# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
from random import randint

guesses = 0
n = randint(1, 9)

while True:
    print(f"\nGuesses: {guesses}")
    print("Guess my number (1-9)")
    u = int(input(": "))

    if u == n:
        print(f"exactly right: {n}!")
        break
    else:
        print("too low" if u < n else "too high")
        guesses += 1
