# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
sentence = str(input("sentence: "))

words = sentence.split(' ')[::-1]
reverse = ' '.join(words)
print(reverse)
