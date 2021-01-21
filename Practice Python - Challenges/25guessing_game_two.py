# https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
from random import randint

def won():
    print("I won!")
    exit()


def game(arr, n, l, z):
    if l >= z:
        print(f"Is {n} your number?")
        ans = int(input("y: 1 | h: 2 | l: 3"))
        if ans == 1:
            won()
        elif ans == 2:
            game(arr[n:], )
        elif ans == 3:
            game(arr[:n], )
        else:
            game(arr, n, l, z)


def run():
    numbers = [x for x in range(101)]
    firstnum = randint(0, 100)
    print("""Number Guessing Game

Pick a number between 0-100. I will try to guess it.

Start [1]
Exit  [0]
    """)
    c = int(input(": "))
    if c == 1:
        game(numbers, firstnum, len(numbers), 0)
    elif c == 0:
        exit()
    else:
        run()


if __name__ == '__main__':
    run()
