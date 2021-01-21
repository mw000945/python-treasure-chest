# https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
def drawBoard(s):
    for x in range(s):
        print("---" * s)
        print("|  " * (s+1))
        print("---" * s)

size = int(input("size: "))
drawBoard(size)
