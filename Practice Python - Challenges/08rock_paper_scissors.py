# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
from os import system

def end():
    again = str(input("Play again? (y/n) >>> "))
    if again.lower().startswith('y'):
        run()
    elif again.lower().startswith('n'):
        exit()
    else:
        print("Not an option, try again!")
        end()


def eval(p1, p2):
    # better solution for this?
    if p1 == p2:
        print("It's a tie!")
    elif p1 == 1 and p2 == 3:
        print(f"{p1} wins: Rock beats Scissors")
    elif p1 == 2 and p2 == 1:
        print(f"{p1} wins: Paper beats Rock")
    elif p1 == 3 and p2 == 2:
        print(f"{p1} wins: Scissors beats Paper")
    elif p2 == 1 and p1 == 3:
        print(f"{p2} wins: Rock beats Scissors")
    elif p2 == 2 and p1 == 1:
        print(f"{p2} wins: Paper beats Rock")
    elif p2 == 3 and p1 == 2:
        print(f"{p2} wins: Scissors beats Paper")
    else:
        print("Error at eval function")
    end()

def run():
    system('clear')
    p1 = int(input("Player1, Rock [1] Paper [2] Scissors [3] >>> "))
    system('clear') # to hide decision of player1
    p2 = int(input("Player2, Rock [1] Paper [2] Scissors [3] >>> "))
    eval(p1, p2)


def start():
    print("""\nWelcome to Rock Paper Scissors!

    Start [1]
    Exit  [0]
    """)
    choice = int(input(">>> "))
    if choice == 1: run()
    elif choice == 0: exit()
    else: start()

if __name__ == '__main__':
    start()
