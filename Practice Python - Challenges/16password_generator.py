# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
import string
from random import choice

characters = string.ascii_letters + string.digits + string.punctuation
length = int(input("length: ")) # determines password strength

password = ''
for x in range(length):
    password += choice(characters)

print(f"password: {password}")
