# https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
from os import chdir
from collections import Counter

FILE = './resources/22name_file.txt'

with open(FILE, 'r') as f:
    names = []
    for name in f:
        name = name.rstrip()
        names.append(name)
    counter = Counter(names)
    for n, c in counter.items():
        print(f"{n}: {c}")

f.close()
