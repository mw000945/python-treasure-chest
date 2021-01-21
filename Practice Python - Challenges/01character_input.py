# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
from datetime import datetime

name, age = str(input("Enter you name and age: ")).split()
current_year = datetime.now().year

year = current_year + (100 - int(age))
print(f"{name}, in the year {year} you will turn 100.")
