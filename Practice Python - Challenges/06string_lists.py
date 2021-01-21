# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
string = str(input("string: "))
print("palindrome" if string == string[::-1] else "not a palindrome")
