# password generator, [a-zA-Z0-9] + punctuation
from random import choice
import string

characters = string.ascii_letters + string.digits + string.punctuation

def run():
    password = ''
    length = int(input("Length: "))
    for x in range(length):
        password += choice(characters)
    print(password)


if __name__ == '__main__':
    run()
